from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, TimeField
from wtforms.validators import DataRequired, Length


class RideForm(FlaskForm):
    vehicle_plate = StringField(
        'vehicle_plate', validators=[DataRequired('Campo obrigatório')]
    )
    passenger_cpf = StringField(
        validators=[
            DataRequired('Campo obrigatório'),
            Length(
                min=11,
                max=11,
                message='O cpf deve possuir exatamente 11 dígitos.',
            ),
        ],
    )
    date = DateField('date', validators=[DataRequired('Campo obrigatório')])
    time = TimeField('time', validators=[DataRequired('Campo obrigatório')])
    distance = FloatField(
        'distance', validators=[DataRequired('Campo obrigatório')]
    )
