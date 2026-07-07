from sqlalchemy.orm import Session

from app.models.user import User
from app.utils.security import hash_password


def seed_users(db: Session):

    users = [
        {
            "name": "Alice",
            "email": "alice@example.com",
            "password": "password123"
        },
        {
            "name": "Bob",
            "email": "bob@example.com",
            "password": "password123"
        }
    ]

    for item in users:

        existing = db.query(User).filter(
            User.email == item["email"]
        ).first()

        if existing:
            continue

        user = User(
            name=item["name"],
            email=item["email"],
            password=hash_password(item["password"])
        )

        db.add(user)

    db.commit()