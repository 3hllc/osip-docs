---
title: Парк и control plane
translation_status: current
source_language: en
---

# Парк и control plane

## Назначение

Парк OSIP и control plane согласованно управляют множеством объектов, сред исполнения Edge, провайдеров и версий развёртывания. Они отделены от локальных данных объекта и критического пути исполнения. Control plane делает ввод в эксплуатацию, конфигурацию, работоспособность, поддержку, аудит, rollout и границы tenants управляемыми в масштабе парка, не превращая удалённый service в владельца локальной безопасности.

## Область действия

Control plane поддерживает inventory и topology fleet; регистрацию sites и edge; lifecycle/configuration Provider-ов; evidence commissioning и asset-binding; распространение policy и automation; versioning, staged rollout, rollback, health, drift, diagnostics, audit, access control, tenant scope и approval workflows. Он может регистрировать экземпляр Home Assistant, MQTT bridge, BACnet Provider или прямой Provider как managed Provider и показывать его health, версию configuration, bindings и provenance.

Он не должен переносить raw высокочастотную telemetry site по умолчанию, выдавать непроверенную удалённую command в critical loop или устранять полномочия локальной policy. Egress данных, remote support и fleet analytics явно классифицируются и авторизуются для каждой capability и tenant.

## Жизненный цикл site

1. Зарегистрировать site и создать его tenant/access boundaries.
2. Зарегистрировать edge runtime и установить management identity с ограниченной целью.
3. Зарегистрировать Provider-ы и обнаружить candidate endpoints.
4. Commission проверенные endpoints в assets OSIP, relationships, capabilities и binding roles.
5. Распространить versioned configuration, policies и automation с критериями приёмки.
6. Наблюдать health, drift, incidents, audit evidence и готовность к recovery.
7. Использовать staged rollout и явный rollback для каждого существенного изменения runtime, Provider-а, policy или contract.

## Полномочия configuration и drift

Control plane владеет проверенной desired configuration; edge фиксирует применённую версию и локально обнаруженный drift. Installer может внести авторизованную аварийную коррекцию, но она должна стать согласованным изменением configuration, а не постоянным неучтённым локальным исключением. Rollout требует compatibility checks для версии edge, версии Provider-а, контракта asset/capability, policy и rollback target.

## Последовательность продукта

Fleet capability — направление продукта, а не предусловие MVP. Reference Apartment создаёт data model и evidence, необходимые для последующей работы с несколькими sites: site scope, стабильные assets, регистрация Provider-ов, версия configuration, версия policy, health, audit и recovery. Выделенная реализация control plane начинается только тогда, когда несколько sites или повторяемые развёртывания Installer Edition создают эксплуатационную необходимость.

## Связанные документы

- [Edge Runtime](edge-runtime.md)
- [Модель физических активов](physical-asset-model.md)
- [Обзор операций](../operations/README.md)
- [Коммерческая стратегия и Installer Edition](../product/commercial-strategy.md)
