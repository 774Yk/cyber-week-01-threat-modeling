"""Intentionally simple local reconnaissance lab server.

This service is deliberately bound to 127.0.0.1 by default and contains only
simulated assets. It is not intended for deployment or use against systems you
do not own or explicitly have permission to test.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

HOST = os.getenv("LAB_HOST", "127.0.0.1")
PORT = int(os.getenv("LAB_PORT", "8080"))

ASSETS = {
    "/": {"name": "local-recon-lab", "status": "ok"},
    "/health": {"service": "lab-server", "status": "healthy"},
    "/api/info": {"version": "1.0.0", "environment": "training", "owner": "local-lab"},
}

class LabHandler(BaseHTTPRequestHandler):
    server_version = "LocalReconLab/1.0"

    def do_GET(self):  # noqa: N802
        payload = ASSETS.get(self.path)
        if payload is None:
            self.send_error(404, "simulated asset not found")
            return
        body = json.dumps(payload, indent=2).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        # Keep lab output deterministic and free from request-header secrets.
        print("LAB", self.command, self.path, args[1])


def main():
    if HOST not in {"127.0.0.1", "localhost"}:
        raise SystemExit("Refusing to bind outside localhost")
    print(f"Serving simulated lab on http://{HOST}:{PORT}")
    HTTPServer((HOST, PORT), LabHandler).serve_forever()

if __name__ == "__main__":
    main()
