#!/usr/bin/env python

from pydantic import BaseModel


class InmuebleBase(BaseModel):
    municipio:str
    fraccionamiento: str
    model: str
    address: str
    price: str
    ground_area: str
    area: str
    bathrooms: str
    rooms: str
    parkings: str


class InmuebleCreate(InmuebleBase):
    pass


class Inmo(InmuebleBase):
    municipio: str

    class Config:
        orm_mode = True
