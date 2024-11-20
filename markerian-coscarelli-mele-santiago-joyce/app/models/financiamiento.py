from peewee import *
from app.modelo_orm import BaseModel
class Financiamiento(BaseModel):
    id=AutoField()
    financiamiento=CharField(unique=True)
    def __str__(self):
        pass
    class Meta:
        db_table = 'financiamiento'