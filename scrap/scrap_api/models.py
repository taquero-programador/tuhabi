#!/usr/bin/env python

from sqlalchemy import Column, String
from database import Base


class Inmo(Base):
    __table__ = "inmuebles"

    municipio = Column(String)
    fraccionamiento = Column(String)
    model = Column(String)
    address = Column(String)
    price = Column(String)
    ground_area = Column(String)
    area = Column(String)
    bathrooms = Column(String)
    rooms = Column(String)
    parkings = Column(String)

