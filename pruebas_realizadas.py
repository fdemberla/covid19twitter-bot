from bs4 import BeautifulSoup


def obtener_pruebas_realizadas():
    print("Extrayendo cantidad de pruebas realizadas...")
    pagina = open("./output/cantidad_de_pruebas.html")

    with pagina as markup:
        soup = BeautifulSoup(markup.read(), "html.parser")

        lista = []

        for tag in soup.findAll("text"):
            lista.append(tag.text.strip())

        objeto = {
            "Positivas": int(lista[1].replace(",", "")),
            "Negativas": int(lista[-1].replace(",", "")),
            "Total_de_Pruebas": int(lista[1].replace(",", ""))
            + int(lista[-1].replace(",", "")),
        }

    return f"""Pruebas realizadas: {objeto.get("Total_de_Pruebas")}
Positivas: {objeto.get("Positivas")}
Negativas: {objeto.get("Negativas")}
#COVID19 #ProtegetePanama #Panama #Coronavirus"""
