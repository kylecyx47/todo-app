from fastapi import FastAPI
from .database import engine
from . import models

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Todo API is running"}

models.Base.metadata.create_all(bind=engine)