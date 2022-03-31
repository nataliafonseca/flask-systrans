from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, TimeField
from wtforms.validators import DataRequired, Length


class ReportForm(FlaskForm):

    initial_date = DateField(
        'initial_date', validators=[DataRequired('Campo obrigatório')]
    )
    final_date = DateField(
        'final_date', validators=[DataRequired('Campo obrigatório')]
    )
