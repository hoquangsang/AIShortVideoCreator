## 🗂️ Cấu trúc thư mục Backend

```plaintext
backend/
├── config/                                 # Cấu hình chung (env, settings)
│   └── settings.py
│
├── app/
│   ├── core/                               # Clean Architecture core
│   │   ├── domain/                         # Entities & Interfaces (business rules)
│   │   ├── application/                    # UseCases / DTOs
│   │   ├── infrastructure/                 # DB, APIs, file systems...
│   │   └── interfaces/                     # HTTP API, CLI, GraphQL, etc.
│
│   ├── context/                            # DI container, lifecycle, middleware
│   │   ├── module.py
│   │   └── lifecycle.py
│   │
│   ├── main.py                             # FastAPI app entrypoint
│   └── __init__.py
│
├── tests/                                  # Unit & integration tests
│
├── run.py                                  # Run entry (e.g. for uvicorn)
├── requirements.txt
└── .env

```

> Được tổ chức theo `Clean architecture`.
```plaintext
[ Schema ]      # interface
    ↓
[  DTO   ]      # application
    ↓
[ Entity ]      # domain
    ↓
[ Model  ]      # infrastructure
```