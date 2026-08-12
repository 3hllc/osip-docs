---
title: Доменная модель
translation_status: current
source_language: en
---

# Доменная модель

## Ограниченный домен

Домен OSIP описывает физическую среду и её намеренное поведение независимо от протоколов и вендоров. Его ключевые понятия: Site, Building, Floor, Space, Zone, Asset, Capability, Binding, Provider, Person, Role, Event, Context, Policy, Intent, Execution Plan, Task и Audit Record. Installation — развёртываемый OSIP runtime, связанный с site; он не является единственным владельцем physical identity.

Site владеет digital twin, поддерживаемыми identity, configuration, policy и эксплуатационной историей. Buildings, floors, spaces и zones дают физический и семантический контекст. Assets предоставляют capabilities через Provider-ы и создают observations. Binding связывает актив OSIP с внешней identity Provider-а, не заменяя его стабильную identity. Policy определяет допустимость intent; Constrained Spatial Reasoning Layer создаёт execution plan; задачи координируют многошаговую работу; audit records сохраняют причину, актора, решение и результат.

## Инварианты

- Стабильные идентификаторы активов OSIP никогда не выводятся только из идентификаторов вендора.
- Binding Provider-а может быть неизвестным или неисправным, не делая недействительным актив или содержащее его пространство.
- Иерархия site и граф отношений активов различны: zones, отношения обслуживания, границы безопасности и зоны доступа могут пересекать дерево вложенности.
- Observation является доказательством, а не командой и не решением авторизации.
- Решение policy связано с версионированной policy и identity или системным актором.
- Запрошенный результат intent отличен от его execution plan, попыток и наблюдаемых результатов.

Адреса, payload и идентификаторы сущностей, специфичные для протокола, остаются внутри моделей Provider-а. Их сопоставление с активом OSIP, capability и binding является явным, проверяемым и аудируемым.
