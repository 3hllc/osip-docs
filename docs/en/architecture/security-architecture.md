# Security Architecture

## Security objective

OSIP protects people, their home, and their data while allowing maintainable installation and support. The initial threat model includes compromised IoT devices, stolen credentials, a malicious or compromised cloud account, accidental installer error, insecure local networks, supply-chain issues, and physical access to local equipment.

## Trust zones

The reference design separates user devices, trusted platform services, IoT/low-trust devices, management tooling, and Internet-facing services. A zone boundary is enforced with network policy and distinct identities—not only by naming a VLAN. Administrative access enters through a controlled management path; devices do not receive unrestricted access to platform services or the Internet.

## Identities and secrets

People, services, adapters, devices where supported, and installer tools use distinct identities. Credentials have minimal scope, rotation/revocation procedures, and storage outside Git. MQTT and APIs enforce authentication and authorization at their own boundary. Shared superuser credentials, hard-coded tokens, and untracked commissioning secrets are prohibited.

## Safety-relevant actions

Actions involving locks, water, electrical isolation, HVAC limits, alarms, and robotics have explicit authorization and audit requirements. Where an automatic action can materially affect safety or access, a documented conservative failure state and manual override are required. AI recommendations follow the controlled action path in the AI architecture; they do not gain direct device control.

## Operations and incident readiness

The installation records authentication failures, privileged configuration changes, command intent and outcome, security-relevant device health, and backup/restore actions. Logs minimise sensitive content and have access/retention rules. A supported deployment documents how to revoke access, isolate a suspected component, restore known-good configuration, and notify the responsible operator.

## Privacy

The design applies data minimisation and local processing by default. Camera, microphone, occupancy, location, and behaviour-derived data have purpose, owner, retention, access, export, and deletion rules before collection. Cloud egress is opt-in by capability and never an implicit consequence of installing a device.
