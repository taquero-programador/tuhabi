#!/usr/bin/env python

#import os
#from pydantic import BaseSettings, Field, SecretStr
#from dotenv import load_dotenv

#load_dotenv()


#class Settings(BaseSettings):
#    url_db: str = os.environ["URL_DATABASE"]
#    user_db: str = os.environ["USER_DB"]
#    pass_db: SecretStr = os.environ["PASS_DB"]


#    class config:
#        env_prefix = ""
#        case_sensite = False
#        env_file = "~/.env"
#        env_file_conding = "utf-8"


#settings = Settings()

DATABASE_URL = "sqlite:///./inmubles.db"
