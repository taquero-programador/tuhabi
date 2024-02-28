#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

<<<<<<< HEAD
SQLALCHEMY_DATABASE_URL = "sqlite:///./inmubles.db"
=======
# from config import DATABASE_URL

SQLALCHEMY_DATABASE_URL = "sqlite:///./inmo.db"
>>>>>>> af63b0abd5b03787b52af9a08defd7e181d8f948

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
