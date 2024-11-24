from peewee import *

from app.modelo_orm import BaseModel

class Barrio(BaseModel):
    id=AutoField()
    barrio= TextField( null=False)
    def __str__(self):
        pass
    class Meta:
        db_table = 'barrio'