---
title: ADR-0007 — AI-Native, Runtime-Optional Operation
status: accepted
date: 2026-08-07
deciders: [OSIP Project]
tags: [ai, privacy, resilience]
---

# ADR-0007 — AI-Native, Runtime-Optional Operation

## Context

AI can improve explanation, recommendations, contextual interpretation, voice interaction, anomaly detection, and task coordination. It can also be unavailable, incorrect, privacy-sensitive, expensive, or hard to audit. Treating it either as an afterthought or as an unbounded controller would be unsafe.

## Decision

AI is architecturally native: it is designed into OSIP context, contracts, policy, evaluation, observability, privacy, and user experience rather than added as an afterthought. AI is runtime-optional: normal automation and safety-relevant local functions remain available without an AI service. AI may recommend or orchestrate only through approved policy and command boundaries. Both local and cloud inference may be used where their data and failure boundaries are documented.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| AI as a separate add-on | Prevents consistent data, security, evaluation, and user-experience design. |
| AI controls devices directly | Bypasses policy, audit, and deterministic safety controls. |
| No AI capability | Fails to prepare the platform for a central long-term product differentiator. |

## Consequences

AI features require explicit user value, informed data handling, offline behaviour, confidence/uncertainty handling, evaluation criteria, and a human override path.
