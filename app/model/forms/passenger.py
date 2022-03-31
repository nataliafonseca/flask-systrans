from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import DataRequired, Length


class DriverForm(FlaskForm):
    cpf = StringField(
        'cpf',
        validators=[
            DataRequired(),
            Length(
                min=11,
                max=11,
                message='O cpf deve possuir exatamente 11 dígitos.',
            ),
        ],
    )
    name = StringField('name', validators=[DataRequired()])
    birth_date = DateField('birth_date', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    state = StringField('state', validators=[DataRequired()])
