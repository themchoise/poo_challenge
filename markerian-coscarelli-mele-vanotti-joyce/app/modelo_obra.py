from peewee import *
from app.modelo_orm import BaseModel
from app.models import Entorno, Etapa, Tipo, AreaResponsable, Barrio,Financiamiento


# MAPEO DEL CSV A LA TABLA
class GestionObraModel(BaseModel):
    entorno = ForeignKeyField(Entorno, backref='entornos')
    nombre = TextField(null=True)
    etapa = ForeignKeyField(Etapa, backref='etapas')
    tipo = ForeignKeyField(Tipo, backref='tipos')
    area_responsable = ForeignKeyField(AreaResponsable, backref='areas_responsables')
    descripcion = TextField(null=True)
    monto_contrato = FloatField(null=True)
    comuna = IntegerField(null=True)
    barrio = ForeignKeyField(Barrio, backref='barrios')
    direccion = TextField(null=True)
    lat = FloatField(null=True)
    lng = FloatField(null=True)
    fecha_inicio = DateField(null=True)
    fecha_fin_inicial = DateField(null=True)
    plazo_meses = IntegerField(null=True, default=0)
    porcentaje_avance = FloatField(null=True)
    imagen_1 = TextField(null=True)
    imagen_2 = TextField(null=True)
    imagen_3 = TextField(null=True)
    imagen_4 = TextField(null=True)
    licitacion_oferta_empresa = TextField(null=True)
    licitacion_anio = IntegerField(null=True)
    contratacion_tipo = TextField(null=True)
    nro_contratacion = TextField(null=True)
    cuit_contratista = TextField(null=True)
    beneficiarios = IntegerField(null=True)
    mano_obra = IntegerField(null=True, default=0)
    compromiso = TextField(null=True)
    destacada = BooleanField(null=True)
    ba_elige = BooleanField(null=True)
    link_interno = TextField(null=True)
    pliego_descarga = TextField(null=True)
    expediente_numero = TextField(null=True)
    estudio_ambiental_descarga = TextField(null=True)
    financiamiento = ForeignKeyField(Financiamiento, backref='financiamiento')


    def __str__(self):
        atributos = ', '.join(f"{key}={value}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({atributos})"
    
    class Meta:
        db_table = 'gestion_obra'
