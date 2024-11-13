from peewee import *
from app.db.database import db


class BaseModel(Model):
        class Meta:
            database = db

