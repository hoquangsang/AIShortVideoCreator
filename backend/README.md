## 🗂️ Cấu trúc thư mục Backend

```plaintext
backend/
├── app/
│   ├── __init__.py                     # Chứa create_app()
│   │
│   ├── domain/                         # Chứa entity + interface (business logic)
│   │   └── ...
│   │
│   ├── application/                    # Layer usecases
│   │   └── ...
│   │
│   ├── infrastructure/                 # Thư viện kỹ thuật
│   │   └── ...
│   │
│   ├── interfaces/                     # Entry point giao tiếp: HTTP, CLI, ...
│   │   └── ...
│   │
│   └── core/
│       └── ...
│
├── utils/
│   └── ...
│
├── config/                             # Config
│   ├── settings.py
│   └── constants.py
│
├── run.py                             # Điểm khởi chạy
├── requirements.txt
└── .env
```

> Được tổ chức theo kiến trúc `Clean architecture`.
```plaintext
[ Schema ]      # interface
    ↓
[  DTO   ]      # application
    ↓
[ Entity ]      # domain
    ↓
[ Model  ]      # infrastructure
```