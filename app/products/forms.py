from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField
from flask_wtf.file import FileField, FileRequired, FileAllowed
##Validaciones en flask  
from wtforms.validators import InputRequired,NumberRange

#Formulario de registro
class NewProductForm(FlaskForm):
    nombre = StringField(validators = [InputRequired(message = "Falta esto rey")],
                         label = "Ingrese nombre: ")
    precio = IntegerField(label="Ingrese precio: ", validators = [InputRequired(message = "El precio gay"),
                                                                 NumberRange(message = "Precio fuera de rango",
                                                                              min = 1000, 
                                                                              max = 10000)])
    imagen = FileField(label = "Cargue imagen del producto", validators = [FileRequired(message="Suba una imagen"), 
                                                                           FileAllowed(["jpg","png"],
                                                                           message = "Tipo de archivo incorrecto")])
    submit = SubmitField("Registrar")