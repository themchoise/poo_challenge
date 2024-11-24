from peewee import *

from app.modelo_orm import BaseModel

class Entorno(BaseModel):
    id=AutoField()
    entorno= TextField( null=False)
    def __str__(self):
        pass
    class Meta:
        db_table = 'entorno'