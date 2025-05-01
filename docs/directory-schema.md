aeryn-backend/
├── app/
│   ├── __init__.py
│   ├── main.py            # Entry point for the FastAPI app
│   ├── api/               # API route definitions
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   ├── core/              # Core config, settings
│   │   ├── __init__.py
│   │   └── config.py      # Pydantic settings
│   ├── models/            # Pydantic models or ORM models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas/           # Request/response schemas
│   │   ├── __init__.py
│   │   └── user_schema.py
│   ├── services/          # Business logic
│   │   ├── __init__.py
│   │   └── user_service.py
│   ├── db/                # Database connection, migrations
│   │   ├── __init__.py
│   │   └── session.py
│   └── utils/             # Helper functions
│       ├── __init__.py
│       └── security.py
├── tests/                 # Unit and integration tests
│   └── test_main.py
├── .env                   # Environment variables
├── .gitignore             # Git ignore rules
├── .python-version        # Python version
├── pyproject.toml         # Project configuration
├── README.md              # Project documentation
└── uv.lock                # Dependency lock file
