from flask import Blueprint

mi_blueprint = Blueprint('mi_blueprint',__name__, url_prefix='/ejemplo')#Nombre del submodelo

@mi_blueprint.route('/prueba') #Se crea la ruta del modulo en especifico
def prueba(): 
    return "Holi"