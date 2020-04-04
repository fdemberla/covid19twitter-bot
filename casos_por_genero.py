from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def obtener_casos_por_genero():
    print("Extrayendo casos por genero...")
    pagina = open("./output/casos_por_genero.html")
    with pagina as markup:
        sopa = BeautifulSoup(markup.read(), "html.parser")

        lista = []

        for tag in sopa.findAll("text"):
            lista.append(tag.text.strip())

        objeto = {"femenino": int(lista[0]), "masculino": int(lista[1])}

        # Data to plot
        labels = "Femenino", "Masculino"
        sizes = [int(lista[0]), int(lista[1])]
        colors = ["pink", "lightblue"]
        # Plot
        plt.pie(
            sizes,
            labels=labels,
            colors=colors,
            autopct="%1.1f%%",
            shadow=True,
            startangle=140,
        )

        plt.axis("equal")
        plt.savefig("./output/graficas/grafica_casos_por_genero.png")

    print("Casos por genero extraidos!")

    return {
        "tweet": f"""Casos por genero:
Femenino: {objeto.get("femenino")}
Masculino: {objeto.get("masculino")}
#COVID19 #Panama #COVIDー19 #ProtegetePanama #QuedateenCasa""",
        "imagen": "./output/graficas/grafica_casos_por_genero.png",
    }


obtener_casos_por_genero()
