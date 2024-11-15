from peewee import *
from app.modelo_orm import BaseModel
class Tipo(BaseModel):
    id=AutoField()
    tipo= CharField(unique=True)
    def __str__(self):
        pass
    class Meta:
        db_table = 'tipo'