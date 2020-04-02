from bs4 import BeautifulSoup


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

        return f"""Rango de Edades
        {informacion}#COVID19 #COVIDー19 #Panama #ProtegetePanama #QuedateEnCasa"""
