#Dependencia para hacer un blueprint/paquete
from flask import Blueprint

#Definir paquete de productos
products = Blueprint ('products', __name__, url_prefix ='/products', template_folder = 'templates')

from . import routes