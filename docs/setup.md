# Local Development Setup

## Requirements

- Windows 11 ARM64
- Python 3.13 ARM64
- uv
- VS Code

## Setup

```bash
uv sync
```

Activate

```powershell
.venv\Scripts\Activate.ps1
```

Run

```bash
uv run uvicorn app.main:app --reload
```