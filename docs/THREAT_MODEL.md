# Threat model

## Scope and assumptions

- The only target is the bundled local service on `127.0.0.1:8080`.
- The operator owns the local machine and has authorization for this lab.
- No credentials, personal data, or real infrastructure are used.

## Assets

| Asset | Security property | Example risk |
|---|---|---|
| Lab service | Availability and integrity | Accidental exposure beyond loopback |
| Recon output | Integrity and confidentiality | Recording sensitive data in reports |
| Source repository | Confidentiality | Committing secrets |

## Abuse cases and mitigations

1. **User supplies a real host to the scanner.** `validate_target` rejects every
   hostname except `localhost` and `127.0.0.1`.
2. **Container escapes the intended network boundary.** Compose binds loopback,
   drops capabilities, enables `no-new-privileges`, and uses a read-only root.
3. **Secrets enter the repository.** A dependency-free security check scans
   tracked files and CI runs secret scanning.
4. **Recon becomes intrusive.** The tool uses a fixed set of four low-impact
   paths and does not brute-force, exploit, persist, or evade detection.
