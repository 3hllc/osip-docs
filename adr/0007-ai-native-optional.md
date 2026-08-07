---
title: ADR-0007 — AI-Native, Optional Operation
status: accepted
date: 2026-08-07
deciders: [OSIP Project]
tags: [ai, privacy, resilience]
---

# ADR-0007 — AI-Native, Optional Operation

## Context

AI can improve explanation, recommendations, contextual interpretation, voice interaction, anomaly detection, and task coordination. It can also be unavailable, incorrect, privacy-sensitive, expensive, or hard to audit. Treating it either as an afterthought or as an unbounded controller would be unsafe.

## Decision

AI is a first-class platform capability with defined context inputs, tool permissions, evaluation, observability, and privacy rules. It may recommend or orchestrate only through approved policy and command boundaries. Normal automation and safety-relevant local functions remain available without AI. Both local and cloud inference may be used where their data and failure boundaries are documented.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| AI as a separate add-on | Prevents consistent data, security, evaluation, and user-experience design. |
| AI controls devices directly | Bypasses policy, audit, and deterministic safety controls. |
| No AI capability | Fails to prepare the platform for a central long-term product differentiator. |

## Consequences

AI features require explicit user value, informed data handling, offline behaviour, confidence/uncertainty handling, evaluation criteria, and a human override path.
