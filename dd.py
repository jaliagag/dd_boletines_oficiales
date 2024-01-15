from datetime import datetime, timedelta
from date_check import today_date_check

import pdfminer
import shutil
import requests
import os
import json

today = datetime.today()
year = today.year
month = today.month
day = today.day

month_letters = today.strftime("%B")
day_letters = today.strftime("%A")
day_number = today.strftime("%d")

dias = {
    "Monday": "lunes",
    "Tuesday": "martes",
    "Wednesday": "miércoles",
    "Thursday": "jueves",
    "Friday": "viernes",
    "Saturday": "sábado",
    "Sunday": "domingo",
}

meses = {
    "January": "enero",
    "February": "febrero",
    "March": "marzo",
    "April": "abril",
    "May": "mayo",
    "June": "junio",
    "July": "julio",
    "August": "agosto",
    "September": "septiembre",
    "November": "noviembre",
    "December": "diciembre",
}

fecha_hoy = f"{dias[day_letters]} {today.day} de {meses[month_letters]} de {year}"
cero_fecha_hoy = f"{dias[day_letters]} {day_number} de {meses[month_letters]} de {year}"

directory = os.listdir(".")

## Create the directory name
directory_name = f"/home/jaliaga/boletin/{year}-{month}-{day}"
temp_dir = f"/home/jaliaga/boletin/temp"
os.makedirs(directory_name, exist_ok=True)
os.makedirs(temp_dir, exist_ok=True)

print(f"Directories '{directory_name}', temp created successfully!")

files = ["primera", "segunda", "tercera", "cuarta"]

# descargar y meter en la carpeta TEMP
for i in files:
    url = f"https://s3.arsat.com.ar/cdn-bo-001/pdf-del-dia/{i}.pdf"
    filename = f"{i}.pdf"

    response = requests.get(url)

    with open(filename, "wb") as f:
        f.write(response.content)

    shutil.move(os.path.join("./", filename), os.path.join(temp_dir, filename))
    print(f"Downloaded file: {filename}")

for g in os.listdir(temp_dir):
    if today_date_check(f"{temp_dir}/{g}", fecha_hoy, cero_fecha_hoy):
        shutil.move(os.path.join(temp_dir, g), os.path.join(directory_name, g))
        #shutil.move(f"temp/{g}", directory_name)
        print(f"el archivo {g} es de hoy {fecha_hoy}")

shutil.rmtree(temp_dir)
