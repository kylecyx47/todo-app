from sqlalchemy.orm import Session
from . import models

def create_task(db: Session, title: str, description: str):
    new_task = models.Task(
        title = title, 
        description = description
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db: Session):
    return db.query(models.Task).all()
