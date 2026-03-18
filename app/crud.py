from sqlalchemy.orm import Session
from . import models

def create_task(db: Session, title: str, description: str):
    new_task = models.Task(title, description)