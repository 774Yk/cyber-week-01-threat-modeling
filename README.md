# Week 1 — Threat Modeling and Reconnaissance in a Local Lab

A reproducible, safety-first cybersecurity portfolio project. It demonstrates
asset inventory, threat modeling, and low-impact reconnaissance against a
bundled HTTP service that is intentionally restricted to loopback.

## Safety boundary

**Use only the included local lab.** The scanner rejects non-local targets and
will not perform reconnaissance against real websites, companies, accounts, or
infrastructure. This repository contains no malware, credential theft,
persistence, DDoS, destructive exploit, or evasion capability.

## Quick start

```bash
python -m unittest discover -s tests -v
python tools/security_checks.py
python tools/recon.py http://127.0.0.1:8080
```

In another terminal, start the lab first:

```bash
python app/lab_server.py
```

Optional Docker run:

```bash
docker compose up --build
python tools/recon.py http://127.0.0.1:8080
docker compose down
```

## Project contents

- `app/lab_server.py` — simulated HTTP assets, loopback-only binding.
- `tools/recon.py` — fixed-scope DNS, TCP, and HTTP discovery.
- `docs/ARCHITECTURE.md` — system architecture.
- `docs/THREAT_MODEL.md` — assets, abuse cases, and mitigations.
- `docs/SECURITY_ASSESSMENT.md` — professional assessment report.
- `tests/` — unit and integration-style tests.
- `.github/workflows/ci.yml` — tests, linting, dependency and secret checks.
- `CURRICULUM_PROGRESS.md` — 12-week portfolio progress.

## Responsible disclosure and ethics

Only test systems you own or have explicit written authorization to assess.
Respect scope, rate limits, privacy, and applicable law. If a real issue is
found in an authorized system, stop safely, preserve minimal evidence, notify
the owner through the agreed channel, and do not disclose it publicly until a
coordinated disclosure plan exists. This project intentionally contains only a
local simulated target.

## CV and LinkedIn

**CV bullet:** Built a safety-constrained Python reconnaissance lab with
localhost target validation, threat modeling, Docker hardening, automated tests,
and CI security checks.

**LinkedIn:** Completed Week 1 of a cybersecurity portfolio curriculum by
building a reproducible local reconnaissance lab, documenting threats and
controls, and enforcing a localhost-only safety boundary through code and CI.

## License

Educational use only; see `LICENSE`.
