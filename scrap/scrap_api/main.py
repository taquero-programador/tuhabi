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


# return one or more items
@app.get("/inmuebles/", response_model=list[schemas.Inmo])
def read_inmos(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    return crud.get_inmo(db, skip=skip, limit=limit)


# return all fracc in municipio
@app.get("/inmuebles/{municipio}", response_model=list[schemas.Inmo])
def read_fracc_in_inmo(municipio: str, db: Session=Depends(get_db)):
    return crud.get_all_fracc_by_inmo(db, municipio=municipio)


# return fracc in municipio
@app.get("/inmuebles/{municipio}/{fraccionamiento}", response_model=list[schemas.Inmo])
def read_inmos_by_fracc(municipio: str, fraccionamiento: str, db: Session=Depends(get_db)):
    return crud.get_inmo_by_fracc(db, municipio=municipio, fraccionamiento=fraccionamiento)
