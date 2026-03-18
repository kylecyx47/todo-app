from fastapi import FastAPI
from .database import engine
from . import models
from fastapi import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import crud

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Todo API is running"}

@app.get("/tasks")
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks

models.Base.metadata.create_all(bind=engine)

