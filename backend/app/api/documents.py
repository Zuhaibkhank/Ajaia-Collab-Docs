from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.document import (
    DocumentCreate,
    DocumentUpdate,
    DocumentResponse,
    ShareRequest
)

from app.services.document_service import (
    create_document,
    get_documents,
    get_document,
    update_document,
    delete_document,
    share_document,
    get_shared_documents,
    can_access_document,
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


# ==========================
# CREATE DOCUMENT
# ==========================
@router.post("/", response_model=DocumentResponse)
def create(
    data: DocumentCreate,
    db: Session = Depends(get_db)
):
    return create_document(
        db=db,
        title=data.title,
        content=data.content,
        owner_id=1      # Hardcoded for now
    )


# ==========================
# GET ALL DOCUMENTS
# ==========================
@router.get("/", response_model=list[DocumentResponse])
def all_documents(
    db: Session = Depends(get_db)
):
    return get_documents(db)


# ==========================
# GET SINGLE DOCUMENT
# ==========================
@router.get("/{document_id}", response_model=DocumentResponse)
def single_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    CURRENT_USER = 1

    doc = can_access_document(
        db,
        document_id,
        CURRENT_USER
    )

    if not doc:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return doc


# ==========================
# UPDATE DOCUMENT
# ==========================
@router.put("/{document_id}", response_model=DocumentResponse)
def update(
    document_id: int,
    data: DocumentUpdate,
    db: Session = Depends(get_db)
):
    CURRENT_USER = 1

    doc = get_document(db, document_id)

    if not doc:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    if doc.owner_id != CURRENT_USER:
        raise HTTPException(
            status_code=403,
            detail="Permission denied"
        )

    doc = update_document(
        db,
        document_id,
        data.title,
        data.content
    )

    return doc

# ==========================
# DELETE DOCUMENT
# ==========================
@router.delete("/{document_id}")
def remove(
    document_id: int,
    db: Session = Depends(get_db)
):
    CURRENT_USER = 1

    doc = get_document(db, document_id)

    if not doc:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    if doc.owner_id != CURRENT_USER:
        raise HTTPException(
            status_code=403,
            detail="Permission denied"
        )

    delete_document(db, document_id)

    return {
        "message": "Document deleted successfully"
    }

# ==========================
# SHARE DOCUMENT
# ==========================
@router.post("/{document_id}/share")
def share(
    document_id: int,
    data: ShareRequest,
    db: Session = Depends(get_db)
):
    result = share_document(
        db=db,
        document_id=document_id,
        user_id=data.user_id
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    if result == "user_not_found":
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if result == "already_shared":
        raise HTTPException(
            status_code=400,
            detail="Document already shared"
        )

    return {
        "message": "Document shared successfully"
    }


# ==========================
# GET SHARED DOCUMENTS
# ==========================
@router.get("/shared/me", response_model=list[DocumentResponse])
def shared_documents(
    db: Session = Depends(get_db)
):
    # Hardcoded user_id=2 for now
    return get_shared_documents(
        db=db,
        user_id=2
    )