"""Tests for the local-only reconnaissance lab.

Author: Y_774
Contact: yassenalhajere@gmail.com
Developer handles: Telegram Y_774 | WhatsApp Y771
"""

import json
import subprocess
import sys
import threading
import unittest
from http.server import HTTPServer
from app.lab_server import LabHandler
from tools.recon import scan, validate_target

class ReconTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), LabHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.port = cls.server.server_port

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def test_local_scan_discovers_simulated_assets(self):
        result = scan(f"http://127.0.0.1:{self.port}")
        self.assertTrue(result["tcp"][str(self.port)])
        self.assertEqual({item["status"] for item in result["http"]}, {200, 404})

    def test_non_local_target_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_target("http://example.com")

    def test_cli_returns_json(self):
        proc = subprocess.run([sys.executable, "tools/recon.py", f"http://127.0.0.1:{self.port}"], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(proc.stdout)["target"], f"http://127.0.0.1:{self.port}")

if __name__ == "__main__":
    unittest.main()
