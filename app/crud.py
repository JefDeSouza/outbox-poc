
from sqlalchemy.orm import Session
from . import models, schemas
from uuid import uuid4

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)

    outbox_event = models.OutboxEvent(
        id=uuid4(),
        aggregate_type="user",
        aggregate_id=str(db_user.id),
        event_type="created",
        payload={"id": str(db_user.id), "name": db_user.name, "email": db_user.email},
    )
    db.add(outbox_event)

    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()
