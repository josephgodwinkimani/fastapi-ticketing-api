# FastAPI Support Ticketing API

A simple support ticketing API built with FastAPI, Prisma, and SQLite. This API allows users to create tickets, add replies, and manage their support requests efficiently.

## Features

- User management (create users)
- Ticket management (create, close, and reply to tickets)
- Logging of all operations and errors
- Database for easy setup and usage

```
fastapi_ticketing_api/
│
├── app/
│ ├── init.py
│ ├── main.py # Entry point for the FastAPI application
│ ├── models.py # Database models (not used directly with Prisma)
│ ├── schemas.py # Pydantic schemas for request and response validation
│ ├── crud.py # CRUD operations for user and ticket management
│ ├── database.py # Database connection setup using Prisma
│ ├── logging_config.py # Logging configuration
│ └── api/
│ ├── init.py
│ └── routes.py # API routes for user and ticket management
│
├── prisma/
│ ├── schema.prisma # Prisma schema definition
│ └── init.py
│
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```

### Getting Started

### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Push the Prisma schema to the database

```bash
cd prisma
prisma db push
```

### 4. Run the FastAPI application

```bash
uvicorn app.main:app --reload
```

See all HTTP Endpoints [here.](http://127.0.0.1:8000/docs)