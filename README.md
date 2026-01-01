# DeskVision Backend

## Run the API (Windows PowerShell)

From the project root (C:\DeskVision), start the FastAPI server with Uvicorn using one of the following commands:

```powershell
# Recommended: use full module path from project root
uvicorn backend.app.main:app --reload

# Alternative: keep shorter import and add app directory to sys.path
uvicorn app.main:app --reload --app-dir backend
```

The server will start on http://127.0.0.1:8000 and live-reload on changes.

## Health Check

Open http://127.0.0.1:8000/ to see:

```json
{"status": "API is running"}
```
