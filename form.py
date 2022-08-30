from http.client import LENGTH_REQUIRED
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea

class Datos(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(),
        Length(min=3, max=15),
    ])
    apellido = StringField('Apellido', validators=[
        DataRequired(),
        Length(min=3, max=20),
    ])
    direccion = StringField('Direccion', widget=TextArea(), validators=[
        Length(max=125),
    ])
    tel = StringField ('Telefono', validators=[
        DataRequired(),
        Length(min=4, max=15),
    ])
    cotizacion = StringField("Cotizacion", widget=TextArea(), validators=[
        DataRequired(),
        Length(min=3)
    ])

    submit = SubmitField("Cotizar")
