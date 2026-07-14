# DealLens OSS v2 Architecture

```
                Browser
                    │
                    ▼
               Uvicorn
                    │
                    ▼
               FastAPI App
                    │
            Versioned Router
                    │
     ┌──────────────┴──────────────┐
     ▼                             ▼
 Company APIs                Filing APIs
     │                             │
     └──────────────┬──────────────┘
                    ▼
                 Services
                    ▼
              Repositories
                    ▼
              PostgreSQL
```

The project follows a layered architecture where every layer has a single responsibility.