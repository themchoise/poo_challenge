from peewee import *
from app.modelo_orm import BaseModel
class Etapa(BaseModel):
    id=AutoField()
    etapa= CharField(unique=True)
    def __str__(self):
        pass
    class Meta:
        db_table = 'etapa'