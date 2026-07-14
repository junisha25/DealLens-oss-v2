ADR-001 — Restart as v2

Why?

Windows ARM64 compatibility issues made continuing v1 a poor long-term choice.

ADR-002 — pg8000 instead of psycopg

Because Windows ARM64 lacks official wheels.

ADR-003 — uvicorn instead of uvicorn[standard]

Because httptools doesn't currently support our platform without native compilation.

