
import time
from sqlalchemy.orm import Session
from sqlalchemy import update
from .database import SessionLocal
from .models import OutboxEvent
from datetime import datetime

def process_outbox():
    db: Session = SessionLocal()
    try:
        events = db.query(OutboxEvent).filter(OutboxEvent.status == "pending").all()

        for event in events:
            print(f"Processing event {event.id}: {event.payload}")

            db.execute(
                update(OutboxEvent)
                .where(OutboxEvent.id == event.id)
                .values(status="processed", processed_at=datetime.utcnow())
            )
            db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    while True:
        process_outbox()
        time.sleep(5)
