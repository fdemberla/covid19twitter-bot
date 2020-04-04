from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()


def obtener_rango_de_edades():
    print("Obteniendo rango de edades!")
    pagina = open("./output/rango_de_edades.html")

    with pagina as markup:
        soup = BeautifulSoup(markup.read(), "html.parser")

        lista = []

        for tag in soup.findAll("text"):
            lista.append(tag.text.strip())
        # Obtener rango de edad
        edades = lista[0::2]
        valores = lista[1::2]

        informacion = ""
        indice = 0

        for rango in edades:
            informacion += f"{rango}: {valores[indice]}\n"
            indice += 1

        y_pos = np.arange(len(valores))

        plt.bar(y_pos, list(map(int, valores)), align="center", alpha=0.5, color="red")
        plt.xticks(y_pos, edades)
        plt.ylabel("Casos")
        plt.xlabel("Edades")
        plt.title("Casos por grupo de edad")

        plt.savefig("./output/graficas/grafica_edades.png")

        return {
            "tweet": f"""Rango de Edades
        {informacion}#COVID19 #COVIDー19 #Panama #ProtegetePanama #QuedateEnCasa""",
            "imagen": "./output/graficas/grafica_edades.png",
        }
