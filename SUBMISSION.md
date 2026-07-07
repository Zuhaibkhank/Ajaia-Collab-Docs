# Submission

## Candidate

**Name:** Zuhaib Khan

---

## Project

Ajaia Collaborative Docs

---

## Live Deployment

Deployment configuration is included.

Due to the assignment time limit (4–6 hours), the production deployment could not be completed before submission.

The application runs locally using the instructions in README.md.

## GitHub Repository

https://github.com/Zuhaibkhank/Ajaia-Collab-Docs

---

## Tech Stack

### Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Passlib
- Uvicorn

### Frontend

- React
- Vite
- Axios
- React Router

---

## Features Implemented

- User Login
- Create Document
- Read Documents
- Update Document
- Delete Document
- Share Document
- Shared Documents
- REST APIs
- PostgreSQL Integration
- Swagger Documentation

---

## APIs

### Authentication

- POST /api/login

### Documents

- GET /api/documents
- POST /api/documents
- GET /api/documents/{id}
- PUT /api/documents/{id}
- DELETE /api/documents/{id}

### Sharing

- POST /api/documents/{id}/share
- GET /api/documents/shared/me

---

## Run Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## Run Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Project Status

All required backend APIs and frontend features have been implemented successfully.
