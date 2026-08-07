# Context Model

## Purpose

Context gives meaning to raw observations. A motion event is not automatically occupancy; a light level is not automatically an instruction to turn on lighting. OSIP derives contextual facts from observations, spatial relationships, time, preferences, and declared policies while preserving provenance and uncertainty.

## Context record

A context record identifies its subject (person, space, zone, object, device, or installation), fact type, value, source evidence, occurrence and expiry timestamps, confidence, derivation method/version, data classification, and owner. A record can be asserted, observed, or inferred. Only asserted and validated physical configuration may change the digital twin baseline; inferred records remain distinct and expire when evidence becomes stale.

## Examples

`osip.space.occupancy-inferred.v1` may state that the reading zone is likely occupied at a confidence of 0.82 based on motion, presence, and time evidence. An automation may use it only within a policy that names its confidence and freshness thresholds. A user preference can refine lighting behaviour but cannot override a leak-protection policy.

## Privacy and control

Context is classified according to sensitivity. Occupancy, identity, camera-derived facts, and behavioural patterns are accessed only by authorised components for a documented purpose. Residents can inspect and correct durable preferences and configuration; derived context is explainable through its evidence references and may be disabled by capability.
