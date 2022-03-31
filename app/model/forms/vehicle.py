from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length


class VehicleForm(FlaskForm):
    plate = StringField(
        'plate', validators=[DataRequired('Campo obrigatório')]
    )
    type = SelectField(
        'Tipo',
        choices=[
            ('Carro', 'Carro'),
            ('Onibus', 'Onibus'),
            ('Van', 'Van'),
        ],
        validators=[DataRequired('Campo obrigatório')],
    )
    car_make = StringField(
        'make', validators=[DataRequired('Campo obrigatório')]
    )
    model = StringField(
        'model', validators=[DataRequired('Campo obrigatório')]
    )
    year = IntegerField(
        'year',
        validators=[
            DataRequired('Campo obrigatório'),
        ],
    )
    passenger_capacity = IntegerField(
        'passenger_capacity',
        validators=[DataRequired('Campo obrigatório')],
    )
    driver_cpf = StringField(
        'driver_cpf',
        validators=[
            DataRequired('Campo obrigatório'),
            Length(
                min=11,
                max=11,
                message='O cpf deve possuir exatamente 11 dígitos.',
            ),
        ],
    )
