from peewee import *
from app.modelo_orm import BaseModel
from app.models import Entorno, Etapa, Tipo, AreaResponsable


# MAPEO DEL CSV A LA TABLA
class GestionObraModel(BaseModel):
    entorno = ForeignKeyField(Entorno, backref='entorno')
    nombre = TextField()
    etapa = ForeignKeyField(Etapa, backref='etapa')
    tipo = ForeignKeyField(Tipo, backref='tipo')
    area_responsable = ForeignKeyField(AreaResponsable, backref='area_responsable')
    descripcion = TextField()
    monto_contrato = TextField()
    date = DateTimeField()
    parcial = BooleanField()
    quantity = IntegerField()
    def __str__(self):
        pass
    class Meta:
        db_table = 'gestion_obra'