# Estructura del microservicio
auth_service/
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   └── protected.py
│   │   └── dependencies.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   │   └── firebase.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── main.py
│   └── __init__.py
│
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_protected.py
│
├── serviceAccountKey.json
├── .env
├── Dockerfile
├── requirements.txt
└── README.md


## Como Van 