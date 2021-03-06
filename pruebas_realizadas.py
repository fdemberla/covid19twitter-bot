from bs4 import BeautifulSoup
import datetime
import csv
import matplotlib.pyplot as plt


now = datetime.datetime.now()
dia_de_hoy = f"{now.day}/{now.month}/{now.year}"


def obtener_pruebas_realizadas():
    print("Extrayendo cantidad de pruebas realizadas...")
    pagina = open("./output/cantidad_de_pruebas.html")

    with pagina as markup:
        soup = BeautifulSoup(markup.read(), "html.parser")

        lista = []

        for tag in soup.findAll("text"):
            lista.append(tag.text.strip())

        objeto = {
            "Fecha": dia_de_hoy,
            "Positivas": int(lista[1].replace(",", "")),
            "Negativas": int(lista[-1].replace(",", "")),
            "Total_de_Pruebas": int(lista[1].replace(",", ""))
            + int(lista[-1].replace(",", "")),
        }

        with open(
            f"./output/base_de_datos/base_de_datos_pruebas_realizadas.csv",
            "a",
            newline="",
        ) as csvfile:
            fieldnames = ["Fecha", "Positivas", "Negativas", "Total_de_Pruebas"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(objeto)

        # Data to plot
        labels = "Negativas", "Positivas"
        sizes = [int(lista[-1].replace(",", "")), int(lista[1].replace(",", ""))]
        colors = ["green", "red"]
        explode = (0.1, 0)  # explode 1st slice

        # Plot
        plt.pie(
            sizes,
            explode=explode,
            labels=labels,
            colors=colors,
            autopct="%1.1f%%",
            shadow=True,
            startangle=140,
        )

        plt.axis("equal")
        plt.savefig("./output/graficas/grafica_pruebas_realizadas.png")

    return {
        "tweet": f"""Pruebas realizadas: {objeto.get("Total_de_Pruebas")}
Positivas: {objeto.get("Positivas")}
Negativas: {objeto.get("Negativas")}
#COVID19 #ProtegetePanama #Panama #Coronavirus""",
        "imagen": "./output/graficas/grafica_pruebas_realizadas.png",
    }
