from bs4 import BeautifulSoup
import datetime
import csv

now = datetime.datetime.now()
dia_de_hoy = f"{now.day}/{now.month}/{now.year}"


def obtener_casos_principales():
    print("Obteniendo casos principales!")
    pagina = open("./output/casos.html")

    def convertir_a_numero(numero):
        return int(numero.replace(",", ""))

    with pagina as markup:
        soup = BeautifulSoup(markup.read(), "html.parser")

        lista = []

        for tag in soup.findAll("text"):
            lista.append(tag.text.strip())

        valores = list(map(convertir_a_numero, lista[1::2]))

        objeto = {
            "fecha": dia_de_hoy,
            "activos": sum(valores) - (valores[2] + valores[0]),
            "recuperados": valores[0],
            "hospitalizados": valores[1],
            "fallecidos": valores[2],
            "aislamiento": valores[3],
            "uci": valores[-1],
            "total": sum(valores),
        }

    with open(
        f"./output/base_de_datos/base_de_datos_totales.csv", "a", newline="",
    ) as csvfile:
        fieldnames = [
            "fecha",
            "activos",
            "recuperados",
            "hospitalizados",
            "fallecidos",
            "aislamiento",
            "uci",
            "total",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(objeto)

    print("Casos principales extraidos con exito!")

    tweet = f"""COVID-19 en Panamá
        
Casos: {objeto.get("total")} - Activos: {objeto.get("activos")}
Hospitalizados: {objeto.get("hospitalizados")} - UCI: {objeto.get("uci")}
Fallecidos: {objeto.get("fallecidos")} - Recuperados: {objeto.get("recuperados")}
Aislamiento: {objeto.get("aislamiento")}

Actualizado cada 24 horas
#Coronavirus #COVID19 #COVIDー19 #Panamá #ProtegetePanama #QuedateenCasa
Fuente: MINSA https://bit.ly/3bDYxIV"""

    return tweet
