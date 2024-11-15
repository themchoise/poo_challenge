from peewee import *

from app.modelo_orm import BaseModel

class ContratacionTipo(BaseModel):
    id=AutoField()
    contratacion_tipo= TextField( null=False)
    def __str__(self):
        pass
    class Meta:
        db_table = 'contratacion_tipo'