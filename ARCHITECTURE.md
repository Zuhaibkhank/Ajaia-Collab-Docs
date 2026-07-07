# Architecture

# Ajaia Collaborative Docs

---

## System Overview

The application follows a client-server architecture.

```
                +----------------------+
                |      React Frontend  |
                +----------+-----------+
                           |
                      Axios HTTP
                           |
                           v
                +----------+-----------+
                |     FastAPI Backend  |
                +----------+-----------+
                           |
                    SQLAlchemy ORM
                           |
                           v
                +----------+-----------+
                |    PostgreSQL DB     |
                +----------------------+
```

---

# Components

## Frontend

Built with React and Vite.

Responsibilities:

- User Login
- Dashboard
- Document Editor
- Document Sharing
- API Communication

Pages:

- Login
- Dashboard
- Editor

Components:

- Navbar
- Sidebar
- DocumentCard
- ShareModal
- EditorToolbar

---

## Backend

Built using FastAPI.

Responsibilities:

- Authentication
- CRUD Operations
- Document Sharing
- Validation
- Business Logic

Modules:

```
app/

api/
services/
models/
schemas/
utils/
db/
```

---

## Database

PostgreSQL stores all application data.

Tables:

### Users

```
id
name
email
password
```

### Documents

```
id
title
content
owner_id
```

### Document Shares

```
id
document_id
user_id
```

Relationships

```
User
   |
   | owns
   |
Documents
   |
   | shared with
   |
DocumentShare
```

---

# API Flow

Login

```
React
   ↓
POST /api/login
   ↓
Authentication
   ↓
User Response
```

Create Document

```
Dashboard
      ↓
POST /api/documents
      ↓
Database
      ↓
Success Response
```

Update Document

```
Editor
    ↓
PUT /api/documents/{id}
    ↓
Database
    ↓
Updated Document
```

Delete Document

```
Dashboard
     ↓
DELETE /api/documents/{id}
     ↓
Database
     ↓
Success
```

Share Document

```
Editor
    ↓
POST /api/documents/{id}/share
    ↓
DocumentShare Table
    ↓
Shared Successfully
```

Shared Documents

```
Dashboard
      ↓
GET /api/documents/shared/me
      ↓
Database
      ↓
Shared Document List
```

---

# Technologies

Frontend

- React
- Vite
- Axios
- React Router

Backend

- FastAPI
- SQLAlchemy
- Pydantic
- Passlib
- Uvicorn

Database

- PostgreSQL

---

# Overall Architecture

```
React UI
    │
    ▼
Axios Requests
    │
    ▼
FastAPI Routes
    │
    ▼
Service Layer
    │
    ▼
SQLAlchemy ORM
    │
    ▼
PostgreSQL
```

---

# Summary

The application uses a clean layered architecture that separates presentation, API routing, business logic, and database access. This structure makes the project modular, maintainable, and easy to extend with additional features in the future.