from peewee import *
from app.modelo_orm import BaseModel
class Licitacion_oferta_empresa(BaseModel):
    id=AutoField()
    licitacion_oferta_empresa= CharField(null = False,unique=True)
    def __str__(self):
        pass
    class Meta:
        db_table = 'licitacion_oferta_empresa'