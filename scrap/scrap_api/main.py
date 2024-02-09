#!/usr/bin/env python

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import database
import crud
import schemas

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("inmuebles/", response_model=list[schemas.Inmo])
def read_inmos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_inmo(db, skip=skip, limit=limit)
