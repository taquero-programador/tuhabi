#!/usr/bin/env python

from pydantic import BaseModel


class InmuebleBase(BaseModel):
    id: int
    municipio: str
    fraccionamiento: str
    model: str
    address: str
    price: int | None
    ground_area: int | None
    area: int | None
    bathrooms: str
    rooms: str
    parkings: str


class InmuebleCreate(InmuebleBase):
    pass


class Inmo(InmuebleBase):
    municipio: str

    class ConfigDict:
        from_attributes = True
