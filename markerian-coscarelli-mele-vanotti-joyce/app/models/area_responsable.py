from peewee import *
from app.modelo_orm import BaseModel

class AreaResponsable(BaseModel):
    id = AutoField()
    area_responsable = CharField()  
    def __str__(self):
        return f"AreaResponsable(id={self.id}, area_responsable='{self.area_responsable}')"

    class Meta:
        db_table = 'area_responsable'
