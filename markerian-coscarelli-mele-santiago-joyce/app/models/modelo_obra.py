from peewee import *
from app.modelo_orm import BaseModel
from app.models import Entorno, Etapa, Tipo, AreaResponsable, Barrio


# MAPEO DEL CSV A LA TABLA
class GestionObraModel(BaseModel):
    entorno = ForeignKeyField(Entorno, backref='entorno')
    nombre = TextField()
    etapa = ForeignKeyField(Etapa, backref='etapa')
    tipo = ForeignKeyField(Tipo, backref='tipo')
    area_responsable = ForeignKeyField(AreaResponsable, backref='area_responsable')
    descripcion = TextField()
    monto_contrato = FloatField()  # Suponiendo que es un monto numérico
    comuna = TextField()
    barrio = ForeignKeyField(Barrio, backref='barrio')
    direccion = TextField()
    lat = FloatField()
    lng = FloatField()
    fecha_inicio = DateField()
    fecha_fin_inicial = DateField()
    plazo_meses = IntegerField()
    porcentaje_avance = FloatField()
    imagen_1 = TextField(null=True)
    imagen_2 = TextField(null=True)
    imagen_3 = TextField(null=True)
    imagen_4 = TextField(null=True)
    licitacion_oferta_empresa = TextField()
    licitacion_anio = IntegerField()
    contratacion_tipo = TextField()
    nro_contratacion = TextField()
    cuit_contratista = TextField()
    beneficiarios = IntegerField()
    mano_obra = IntegerField()
    compromiso = TextField()
    destacada = BooleanField()
    ba_elige = BooleanField()
    link_interno = TextField(null=True)
    pliego_descarga = TextField(null=True)
    expediente_numero = TextField()
    estudio_ambiental_descarga = TextField(null=True)
    financiamiento = TextField()

    def __str__(self):
        return f"{self.nombre} - {self.etapa} ({self.fecha_inicio} a {self.fecha_fin_inicial})"

    class Meta:
        db_table = 'gestion_obra'
