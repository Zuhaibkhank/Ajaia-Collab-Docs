from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.documents import router as document_router
from app.db.database import Base, engine
from app.db.database import SessionLocal
from app.services.seed import seed_users
import app.models.user
import app.models.document
import app.models.share

from app.api.auth import router as auth_router

Base.metadata.create_all(bind=engine)

db = SessionLocal()
seed_users(db)
db.close()

app = FastAPI(
    title="Ajaia Collaborative Docs API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(document_router, prefix="/api")

app.include_router(auth_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Ajaia Collaborative Docs API Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}