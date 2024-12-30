from flask import Blueprint, render_template, request
from .forms import YearForm
from .utils import fetch_uf_data, process_uf_data
import json



import json
from decimal import Decimal
from datetime import datetime

def custom_default(obj):
    """Convierte Decimal a float y datetime a string."""
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d')  # Formato de fecha YYYY-MM-DD
    raise TypeError(f"Type {type(obj)} not serializable")

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    form = YearForm()
    data = {}
    json_data = None  # Inicializar con None u otro valor predeterminado

    if form.validate_on_submit():        
        year = form.year.data
        raw_data = fetch_uf_data(year)
        data = process_uf_data(raw_data)
        json_data = json.dumps(data, default=custom_default)

    return render_template("index.html", form=form, data=json_data)
