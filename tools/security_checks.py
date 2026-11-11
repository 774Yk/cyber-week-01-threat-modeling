"""Dependency-free guardrails for this educational repository.

Author: Y_774
Contact: yassenalhajere@gmail.com
Developer handles: Telegram Y_774 | WhatsApp Y771
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = re.compile(r"(?i)(password\s*=|api[_-]?key\s*=|secret\s*=|BEGIN (RSA|OPENSSH|EC) PRIVATE KEY)")
NETWORK_TARGETS = re.compile(r"(?i)https?://(?!127\.0\.0\.1|localhost|\{)")

failures = []
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.name == "security_checks.py":
        continue
    text = path.read_text(errors="ignore")
    if FORBIDDEN.search(text):
        failures.append(f"possible secret pattern: {path}")
    # Runtime code and container configuration must not contain external targets.
    # Tests may mention a non-local URL solely to verify rejection behavior.
    if (path.parts[-2:] in [("app", path.name), ("tools", path.name)] or path.name in {"Dockerfile", "docker-compose.yml"}) and NETWORK_TARGETS.search(text):
        failures.append(f"non-local URL in runtime-controlled file: {path}")
if failures:
    raise SystemExit("\n".join(failures))
print("security checks passed: no obvious secrets or non-local runtime targets")
