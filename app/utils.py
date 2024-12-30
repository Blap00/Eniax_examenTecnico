import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from decimal import Decimal
from collections import defaultdict

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave API desde las variables de entorno
API_KEY = os.getenv("API_KEY")

def fetch_uf_data(year):
    """Fetch UF data from CMF API."""
    url = f"https://api.cmfchile.cl/api-sbifv3/recursos_api/uf/{year}?apikey={API_KEY}&formato=json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

from collections import defaultdict
from datetime import datetime
from decimal import Decimal

def process_uf_data(data):
    """Process UF data to extract required information."""
    
    # Parsear los valores de UF y fechas
    uf_data = [
        {
            "valor": Decimal(item["Valor"].replace(".", "").replace(",", ".")),
            "fecha": datetime.strptime(item["Fecha"], "%Y-%m-%d")
        }
        for item in data["UFs"]
    ]
    
    # Agrupar por mes y calcular el promedio mensual
    monthly_data = defaultdict(list)
    for item in uf_data:
        month_key = item["fecha"].strftime("%Y-%m (%b)")  # Clave del mes en formato YYYY-MM
        monthly_data[month_key].append(item["valor"])

    # Calcular promedio mensual y variación
    monthly_variations = []
    for month, values in monthly_data.items():
        avg_value = sum(values) / len(values)  # Promedio mensual
        start_value = values[0]  # Primer valor del mes
        end_value = values[-1]  # Último valor del mes
        variation = end_value - start_value  # Variación entre inicio y fin del mes
        
        # Añadir la información de cada mes con el índice
        monthly_variations.append({
            "index": len(monthly_variations) + 1,  # Añadir índice
            "month": month,
            "start": start_value,
            "end": end_value,
            "avg": avg_value,
            "variation": variation
        })

    # Ordenar las variaciones mensuales por fecha (mes) en orden ascendente
    monthly_variations = sorted(monthly_variations, key=lambda x: datetime.strptime(x["month"], "%Y-%m (%b)"))

    # Clasificar y ordenar los meses por variación
    increasing = sorted(
        [m for m in monthly_variations if m["variation"] > 0],
        key=lambda x: x["variation"]
    )
    decreasing = sorted(
        [m for m in monthly_variations if m["variation"] < 0],
        key=lambda x: x["variation"], reverse=True
    )
    no_change = sorted(
        [m for m in monthly_variations if m["variation"] == 0],
        key=lambda x: datetime.strptime(x["month"], "%Y-%m (%b)").strftime("%B")
    )

    # Identificar el mes con el valor máximo y mínimo
    max_value = max(uf_data, key=lambda x: x["valor"])
    min_value = min(uf_data, key=lambda x: x["valor"])

    # Añadir tipo de variación y clasificación (Ascendente, Descendente, Sin Variación)
    for month_variation in increasing:
        month_variation["type"] = "Acendente"
    for month_variation in decreasing:
        month_variation["type"] = "Descendente"
    for month_variation in no_change:
        month_variation["type"] = "Sin Variación"
    
    return {
        "increasing": increasing,
        "decreasing": decreasing,
        "no_change": no_change,
        "max_value": max_value,
        "min_value": min_value,
    }


# Uso de ejemplo
if __name__ == "__main__":
    year = 2023
    uf_data = fetch_uf_data(year)
    if uf_data:
        print("Datos de la UF procesados:", process_uf_data(uf_data))
