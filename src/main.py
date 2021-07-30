from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
import datetime
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"Hello" : "World"}


@app.get("/dataset/", response_model=List[schemas.Dataset])
def read_dataset(date: Optional[datetime.date] = None, channel : Optional[str] = None, \
                   country: Optional[str] = None, os : Optional[str] = None, impressions : Optional[int] = None, clicks : Optional[int] = None, \
                  installs : Optional[int] = None, spend : Optional[float]  = None, revenue: Optional[float]  = None, skip: int = 0, limit: int = 1000,\
                  db: Session = Depends(get_db)):
    #datasets = crud.get_datasets(db, date, channel, country, os, impressions, clicks, installs, spend, revenue, skip=skip, limit=limit)
    if os :
        datasets = db.query(models.Dataset).filter(models.Dataset.os == os).offset(skip).limit(limit).all()
    else:
        datasets = db.query(models.Dataset).offset(skip).limit(limit).all()
    return datasets
