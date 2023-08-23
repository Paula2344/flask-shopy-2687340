#dependencia de flask
from flask import Flask

#Dependencia de configuracion 
from .config import Config #El punto es para indicarle a python que los archivos estan en el mismo paquete

#dependencia de modelos
from flask_sqlalchemy import SQLAlchemy

#dependencia de las migraciones
from flask_migrate import Migrate

#Importar el modulo 
from .mi_blueprint import mi_blueprint

#Importar el modulo 
from app.products import 

#Dependencia de boostrap
from  flask_bootstrap import Bootstrap

#crear el objeto flask
app = Flask(__name__)

#Configuracion del objeto flask
app.config.from_object(Config)

#Vincular submodulos del proyecto
app.register_blueprint(mi_blueprint)
app.register_blueprint(products)

#crear el objeto de modelos:

db=SQLAlchemy(app)
#crear el obejeto de migracion 
migrate=Migrate(app,db)

#Crear objeto bootstrap
bootstrap = Bootstrap(app)

#Importar los modelos
from .models import Cliente,Venta,Detalle,Producto


