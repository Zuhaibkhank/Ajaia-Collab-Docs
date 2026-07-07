# Ajaia Collaborative Docs

A collaborative document editing application built using FastAPI, React, PostgreSQL and SQLAlchemy.

---

# Features

- User Login
- Create Document
- Edit Document
- Delete Document
- Share Document
- View Shared Documents
- REST APIs
- PostgreSQL Database
- Swagger API Documentation

---

# Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Passlib
- Uvicorn

## Frontend

- React
- Vite
- Axios
- React Router

---

# Project Structure

```
Ajaia-Collab-Docs
│
├── backend
│   ├── app
│   ├── requirements.txt
│   └── main.py
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── README.md
├── SUBMISSION.md
├── AI_WORKFLOW.md
└── ARCHITECTURE.md
```

---

# Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend

```
http://localhost:5173
```

---

# Available APIs

Authentication

```
POST /api/login
```

Documents

```
GET /api/documents
POST /api/documents
GET /api/documents/{id}
PUT /api/documents/{id}
DELETE /api/documents/{id}
```

Sharing

```
POST /api/documents/{id}/share
GET /api/documents/shared/me
```

---

# Author

Zuhaib Khan