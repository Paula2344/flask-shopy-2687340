from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField,

#Formulario de registro
class NewProductForm(FlaskForm):
    nombre = StringField("Ingrese nombre: ")
    precio = StringField("Ingrese precio: ")
    submit = SubmitField("Registrar")