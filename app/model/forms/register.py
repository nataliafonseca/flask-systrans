from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
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
