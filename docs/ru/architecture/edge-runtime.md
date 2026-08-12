---
title: Edge Runtime
translation_status: current
source_language: en
---

# Edge Runtime

## Назначение

OSIP Edge Runtime — среда исполнения на локальной площадке для объявленных Local First-функций. Она получает канонические события, проецирует релевантное состояние, содержит локально необходимую часть Constrained Spatial Reasoning Layer, оценивает назначенные политики, исполняет детерминированные планы и выпускает команды через подходящих провайдеров. Это продуктовая граница: объект остаётся безопасно управляемым, когда недоступны WAN, cloud services, AI services или парк/control plane.

## Ответственность

- Поддерживать site-scoped подмножество bindings активов, capabilities, отношений, policies, desired state и scope авторизации, требуемое для локальной работы.
- Потреблять и публиковать канонические events и commands через выбранный локальный transport OSIP.
- Исполнять локальный workflow CSRL, детерминированные планы, проверку команд, оценку health и буферизацию audit для назначенных локальных функций.
- Обеспечивать консервативную деградацию и manual override для действий, критичных для безопасности или бизнеса.
- Сверять configuration, policy, software versions и evidence audit с fleet/control plane при наличии связи.

Для объявленного критического пути edge runtime не требует наличия Home Assistant. Home Assistant может работать параллельно как Provider, источник discovery, dashboard или платформа некритичной automation. Сбой Provider-а формирует явное degraded state; он не переносит полномочия молча на несвязанный компонент.

## Контракт локальной непрерывности

Каждая поддерживаемая capability объявляет, является ли она `edge-required`, `edge-preferred`, `centrally-assisted` или `cloud-enhanced`. Для `edge-required` capability развёртывание документирует локальные inputs, bindings Provider-ов, policies, command path, evidence проверки, состояние при сбое, manual override, recovery objective и outage test. Одного cache недостаточно для Local First: edge должен обладать достаточной актуальной авторизованной configuration и исполнимой logic, чтобы действовать безопасно.

## Разделение с control plane

Fleet/control plane распространяет проверенные configuration и policy, регистрирует sites и Provider-ы, координирует rollout и получает operational evidence. Он никогда не становится синхронной зависимостью заявленного критического control loop site. Во время отключения edge исполняет последнюю валидную назначенную configuration, фиксирует drift и audit data, а при возвращении связи сверяет их через явный версионированный процесс.

## Минимальные evidence reference deployment

Reference Apartment должна продемонстрировать хотя бы один сквозной workflow `edge-required`, использующий канонический event, mapping asset/capability, локальную policy, детерминированное исполнение, наблюдаемое завершение и outage test, исключающий WAN и Home Assistant из обязательного пути. Test evidence включает command latency, поведение при сбое, шаги восстановления, audit record и известные ограничения.

## Связанные документы

- [Слой ограниченного пространственного рассуждения](constrained-spatial-reasoning-layer.md)
- [Намерения, политики и исполнение](intent-policy-and-execution.md)
- [Провайдеры интеграций](integration-providers.md)
- [Архитектура развёртывания](deployment-architecture.md)
- [Развёртывание и восстановление](../operations/deployment-and-recovery.md)
