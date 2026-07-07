from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.db.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, default="")
    owner_id = Column(Integer, ForeignKey("users.id"))