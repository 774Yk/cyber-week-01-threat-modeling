# Security assessment report

**Assessment type:** local threat-model and reconnaissance exercise  
**Scope:** bundled service only, loopback interface  
**Date:** 2026-10-14  
**Severity convention:** Informational / Low / Medium / High / Critical

## Executive summary

The lab intentionally exposes three JSON resources and a simulated 404 path for
safe discovery practice. The scanner enforces a localhost-only target policy.
No exploitable finding was intentionally introduced beyond the educational
metadata exposed by `/api/info`.

## Findings

| ID | Severity | Finding | Recommendation | Status |
|---|---|---|---|---|
| F-001 | Informational | `/api/info` returns training metadata | Avoid returning metadata in production services | Accepted for lab |
| F-002 | Low | HTTP service is unauthenticated | Keep the service loopback-only; add auth in any authorized future exercise | Mitigated by scope |

## Evidence and validation

- Automated tests verify discovery, JSON output, and rejection of non-local targets.
- Static checks verify compilation and scan for obvious secrets and non-local URLs.
- Container hardening is declared in `docker-compose.yml`.

## Limitations

This is not a production penetration test. It does not assess external assets,
credentialed flows, or infrastructure outside the explicitly authorized lab.
