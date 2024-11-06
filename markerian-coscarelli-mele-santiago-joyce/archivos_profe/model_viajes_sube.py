from peewee import *

sqlite_db = SqliteDatabase('./importar_csv_a_base_datos/viajes_sube.db', pragmas={'journal_mode': 'wal'})
try:
    sqlite_db.connect()
except OperationalError as e:
    print("Error al conectar con la BD.", e)
    exit()

class BaseModel(Model):
    class Meta:
        database = sqlite_db

class TipoTransporte(BaseModel):
    nombre = CharField(unique=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'tipos_transporte'

class ViajeSube(BaseModel):
    date = DateTimeField()
    parcial = BooleanField()
    quantity = IntegerField()
    tipo_transporte = ForeignKeyField(TipoTransporte, backref='tipo_transporte')
    def __str__(self):
        pass
    class Meta:
        db_table = 'viajes'

#Creamos las tablas correspondientes a las clases del modelo
sqlite_db.create_tables([TipoTransporte, ViajeSube])