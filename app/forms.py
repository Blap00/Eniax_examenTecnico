from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from datetime import datetime

class YearForm(FlaskForm):
    current_year = datetime.now().year
    year_choices = [(str(year), str(year)) for year in range(1990, current_year + 1)]

    year = SelectField("Seleccione el año", choices=year_choices)
    submit = SubmitField("Consultar")
