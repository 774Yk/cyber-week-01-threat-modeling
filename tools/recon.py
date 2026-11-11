"""Safe reconnaissance helper restricted to localhost targets.

Author: Y_774
Contact: yassenalhajere@gmail.com
Developer handles: Telegram Y_774 | WhatsApp Y771
"""
from __future__ import annotations
import argparse
import json
import socket
import urllib.error
import urllib.request
from urllib.parse import urlparse

ALLOWED_HOSTS = {"127.0.0.1", "localhost"}
PATHS = ["/", "/health", "/api/info", "/does-not-exist"]


def validate_target(target: str) -> tuple[str, int]:
    parsed = urlparse(target)
    if parsed.scheme != "http" or parsed.hostname not in ALLOWED_HOSTS:
        raise ValueError("Target must be an http URL on localhost or 127.0.0.1")
    port = parsed.port or 80
    if not 1 <= port <= 65535:
        raise ValueError("Invalid port")
    return parsed.hostname, port


def scan(target: str) -> dict:
    host, port = validate_target(target)
    base = f"http://{host}:{port}"
    result = {"target": base, "dns": {}, "tcp": {}, "http": []}
    result["dns"][host] = socket.gethostbyname(host)
    with socket.socket() as sock:
        sock.settimeout(1)
        result["tcp"][str(port)] = sock.connect_ex((host, port)) == 0
    for path in PATHS:
        try:
            with urllib.request.urlopen(base + path, timeout=2) as response:
                result["http"].append({"path": path, "status": response.status})
        except urllib.error.HTTPError as exc:
            result["http"].append({"path": path, "status": exc.code})
    return result


def main():
    parser = argparse.ArgumentParser(description="Recon only the bundled localhost lab")
    parser.add_argument("target", nargs="?", default="http://127.0.0.1:8080")
    args = parser.parse_args()
    print(json.dumps(scan(args.target), indent=2))

if __name__ == "__main__":
    main()
