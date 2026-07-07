from sqlalchemy.orm import Session
from app.models.document import Document
from app.models.share import DocumentShare

def create_document(db: Session, title: str, content: str, owner_id: int):
    doc = Document(
        title=title,
        content=content,
        owner_id=owner_id
    )

    db.add(doc)
    db.commit()
    db.refresh(doc)

    return doc


def get_documents(db: Session):
    return db.query(Document).all()


def get_document(db: Session, document_id: int):
    return db.query(Document).filter(Document.id == document_id).first()


def update_document(db: Session, document_id: int, title: str, content: str):
    doc = get_document(db, document_id)

    if not doc:
        return None

    doc.title = title
    doc.content = content

    db.commit()
    db.refresh(doc)

    return doc


def delete_document(db: Session, document_id: int):
    doc = get_document(db, document_id)

    if not doc:
        return False

    # Delete all share records first
    db.query(DocumentShare).filter(
        DocumentShare.document_id == document_id
    ).delete()

    # Delete document
    db.delete(doc)

    db.commit()

    return True

from app.models.share import DocumentShare
from app.models.user import User


def share_document(db: Session, document_id: int, user_id: int):
    document = db.query(Document).filter(Document.id == document_id).first()

    if not document:
        return None

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return "user_not_found"

    already = (
        db.query(DocumentShare)
        .filter(
            DocumentShare.document_id == document_id,
            DocumentShare.user_id == user_id
        )
        .first()
    )

    if already:
        return "already_shared"

    share = DocumentShare(
        document_id=document_id,
        user_id=user_id
    )

    db.add(share)
    db.commit()
    db.refresh(share)

    return share


def get_shared_documents(db: Session, user_id: int):
    return (
        db.query(Document)
        .join(
            DocumentShare,
            Document.id == DocumentShare.document_id
        )
        .filter(DocumentShare.user_id == user_id)
        .all()
    )

from app.models.share import DocumentShare


def can_access_document(db: Session, document_id: int, user_id: int):
    doc = get_document(db, document_id)

    if not doc:
        return None

    if doc.owner_id == user_id:
        return doc

    shared = (
        db.query(DocumentShare)
        .filter(
            DocumentShare.document_id == document_id,
            DocumentShare.user_id == user_id
        )
        .first()
    )

    if shared:
        return doc

    return None