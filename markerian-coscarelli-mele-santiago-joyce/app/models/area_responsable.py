from peewee import *
from app.modelo_orm import BaseModel
class AreaResponsable(BaseModel):
    id=AutoField()
    area_responsable= CharField(unique=True)
    def __str__(self):
        pass
    class Meta:
        db_table = 'area_responsable'