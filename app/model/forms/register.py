from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired('Campo obrigatório')]
    )
    password = PasswordField(
        'password', validators=[DataRequired('Campo obrigatório')]
    )
    cpf = StringField(
        'cpf',
        validators=[
            DataRequired('Campo obrigatório'),
            Length(
                min=11,
                max=11,
                message='O cpf deve possuir exatamente 11 dígitos.',
            ),
        ],
    )
    name = StringField('name', validators=[DataRequired('Campo obrigatório')])
    birth_date = DateField(
        'birth_date', validators=[DataRequired('Campo obrigatório')]
    )
    address = StringField(
        'address', validators=[DataRequired('Campo obrigatório')]
    )
