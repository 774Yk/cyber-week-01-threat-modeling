# Architecture

```text
+----------------------+       HTTP on loopback       +----------------------+
| tools/recon.py       | ---------------------------> | app/lab_server.py    |
| safe recon client    |                              | simulated assets     |
+----------------------+                              +----------------------+
          |
          +--> JSON output for assessment evidence
```

The service binds to `127.0.0.1` by default. Docker Compose additionally binds
only the host loopback interface, drops Linux capabilities, uses a read-only
filesystem, and runs as a non-root UID.
