/* Opens diagrams in an accessible, zoomable modal without external UI libraries. */
(() => {
  const MIN_ZOOM = 0.5;
  const MAX_ZOOM = 4;
  const ZOOM_STEP = 0.25;
  let dialog;
  let canvas;
  let viewport;
  let title;
  let zoom = 1;
  let baseWidth = 0;
  let returnAnchor;
  let movedDiagram;

  function diagramFor(element) {
    const plantUml = element.closest(".md-content img[src$='.svg']");
    if (plantUml) return plantUml;

    const mermaid = element.closest(".md-content .mermaid");
    return mermaid || null;
  }

  function describe(diagram) {
    return diagram.getAttribute("alt") || diagram.closest(".mermaid")?.getAttribute("data-title") || "Diagram";
  }

  function makeDiagramsFocusable(root = document) {
    const selector = ".md-content img[src$='.svg'], .md-content .mermaid";
    const diagrams = [
      ...(root.matches?.(selector) ? [root] : []),
      ...root.querySelectorAll(selector),
    ];
    diagrams.forEach((diagram) => {
      diagram.tabIndex = 0;
      diagram.setAttribute("role", "button");
      diagram.setAttribute("aria-label", `Open ${describe(diagram)} in diagram viewer`);
    });
  }

  function setZoom(nextZoom) {
    zoom = Math.min(MAX_ZOOM, Math.max(MIN_ZOOM, Math.round(nextZoom * 100) / 100));
    const diagram = canvas.firstElementChild;
    if (!diagram) return;
    if (movedDiagram) {
      diagram.style.zoom = zoom;
    } else {
      diagram.style.width = `${Math.round(baseWidth * zoom)}px`;
      diagram.style.maxWidth = "none";
    }
    dialog.querySelector("[data-zoom-readout]").textContent = `${Math.round(zoom * 100)}%`;
  }

  function restoreMovedDiagram() {
    if (!movedDiagram || !returnAnchor) return;
    movedDiagram.style.zoom = "";
    returnAnchor.replaceWith(movedDiagram);
    movedDiagram = undefined;
    returnAnchor = undefined;
  }

  function ensureDialog() {
    if (dialog) return;
    dialog = document.createElement("dialog");
    dialog.className = "osip-diagram-lightbox";
    dialog.innerHTML = `
      <div class="osip-diagram-lightbox__toolbar">
        <span class="osip-diagram-lightbox__title"></span>
        <button class="osip-diagram-lightbox__button" type="button" data-zoom-out aria-label="Zoom out">−</button>
        <span data-zoom-readout aria-live="polite">100%</span>
        <button class="osip-diagram-lightbox__button" type="button" data-zoom-in aria-label="Zoom in">+</button>
        <button class="osip-diagram-lightbox__button" type="button" data-zoom-reset>Reset</button>
        <button class="osip-diagram-lightbox__button" type="button" data-close aria-label="Close diagram">Close</button>
      </div>
      <div class="osip-diagram-lightbox__viewport">
        <div class="osip-diagram-lightbox__canvas"></div>
      </div>`;
    document.body.append(dialog);
    canvas = dialog.querySelector(".osip-diagram-lightbox__canvas");
    viewport = dialog.querySelector(".osip-diagram-lightbox__viewport");
    title = dialog.querySelector(".osip-diagram-lightbox__title");

    dialog.querySelector("[data-zoom-out]").addEventListener("click", () => setZoom(zoom - ZOOM_STEP));
    dialog.querySelector("[data-zoom-in]").addEventListener("click", () => setZoom(zoom + ZOOM_STEP));
    dialog.querySelector("[data-zoom-reset]").addEventListener("click", () => setZoom(1));
    dialog.querySelector("[data-close]").addEventListener("click", () => dialog.close());
    dialog.addEventListener("close", restoreMovedDiagram);
    viewport.addEventListener("wheel", (event) => {
      if (!event.ctrlKey && !event.metaKey) return;
      event.preventDefault();
      setZoom(zoom + (event.deltaY < 0 ? ZOOM_STEP : -ZOOM_STEP));
    }, { passive: false });
  }

  function open(diagram) {
    ensureDialog();
    const isRenderedMermaid = diagram.matches("div.mermaid");
    if (isRenderedMermaid) {
      returnAnchor = document.createComment("OSIP Mermaid diagram location");
      diagram.replaceWith(returnAnchor);
      canvas.replaceChildren(diagram);
      movedDiagram = diagram;
    } else {
      const copy = diagram.cloneNode(true);
      copy.removeAttribute("id");
      copy.removeAttribute("tabindex");
      copy.removeAttribute("role");
      canvas.replaceChildren(copy);
      movedDiagram = undefined;
    }
    title.textContent = describe(diagram);
    dialog.showModal();
    baseWidth = Math.max(320, Math.min(diagram.getBoundingClientRect().width, viewport.clientWidth - 32));
    setZoom(1);
    viewport.scrollTo({ top: 0, left: 0 });
  }

  document.addEventListener("click", (event) => {
    const diagram = diagramFor(event.target);
    if (!diagram || dialog?.open) return;
    event.preventDefault();
    open(diagram);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key !== "Enter" && event.key !== " ") return;
    const diagram = diagramFor(event.target);
    if (!diagram || dialog?.open) return;
    event.preventDefault();
    open(diagram);
  });

  makeDiagramsFocusable();
  new MutationObserver((records) => {
    records.forEach((record) => record.addedNodes.forEach((node) => {
      if (node.nodeType === Node.ELEMENT_NODE) makeDiagramsFocusable(node);
    }));
  }).observe(document.body, { childList: true, subtree: true });
})();
