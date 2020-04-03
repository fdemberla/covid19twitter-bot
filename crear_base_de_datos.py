import datetime
import csv

now = datetime.datetime.now()
dia_de_hoy = f"{now.day}/{now.month}/{now.year}"

with open(
    "./output/base_de_datos/base_de_datos_pruebas_realizadas.csv", "w"
) as csvfile:
    filewriter = csv.writer(
        csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
    )
    filewriter.writerow(["Fecha", "Pruebas Positivas", "Pruebas Negativas", "Total"])
