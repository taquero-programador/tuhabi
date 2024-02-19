#!/usr/bin/env python

from sqlalchemy import Column, Text, Integer
from database import Base


class Inmo(Base):
    __tablename__ = "inmuebles"

    id = Column(Integer, primary_key=True, index=True)
    municipio = Column(Text)
    fraccionamiento = Column(Text)
    model = Column(Text)
    address = Column(Text)
    price = Column(Integer)
    ground_area = Column(Integer)
    area = Column(Integer)
    bathrooms = Column(Text)
    rooms = Column(Text)
    parkings = Column(Text)

