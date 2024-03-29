#!/usr/bin/env python

from sqlalchemy.orm import Session
from models import Inmo


# get all inmos
def get_inmo(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Inmo).offset(skip).limit(limit).all()


def get_all_fracc_by_inmo(db: Session, municipio: str):
    return db.query(Inmo).filter(Inmo.municipio==municipio).all()


def get_inmo_by_fracc(db: Session, municipio: str, fraccionamiento: str):
    return db.query(Inmo).filter(Inmo.municipio==municipio, Inmo.fraccionamiento==fraccionamiento).all()


def get_model(db: Session, municipio: str, fraccionamiento: str, model: str):
    return db.query(Inmo).filter(Inmo.municipio==municipio, Inmo.fraccionamiento==fraccionamiento, Inmo.model==model).first()
