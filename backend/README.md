## 🗂️ Cấu trúc thư mục Backend

```plaintext
backend/
├── config/                                 # Cấu hình ứng dụng
│
├── app/
│   ├── domain/                             # Entities và interfaces (business rules)
│   ├── application/                        # Use cases / DTO / Service logic
│   ├── infrastructure/                     # Tích hợp kỹ thuật: ORM, DB, external APIs
│   ├── interfaces/                         # Giao tiếp bên ngoài: HTTP API, CLI, ...
│   │
│   ├── context/                            # Chứa app lifecycle
│   ├── dependencies/                       # Chứa container dependency
│   │
│   └── main.py                             # Điểm vào chính của app (FastAPI entry)
│
├── tests/                                  # Thư mục test
│
├── run.py                                  # Điểm khởi chạy chính
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