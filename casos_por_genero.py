from bs4 import BeautifulSoup


def obtener_casos_por_genero():
    print("Extrayendo casos por genero...")
    pagina = open("./output/casos_por_genero.html")
    with pagina as markup:
        sopa = BeautifulSoup(markup.read(), "html.parser")

        lista = []

        for tag in sopa.findAll("text"):
            lista.append(tag.text.strip())

        objeto = {
            "femenino": int(lista[0]),
            "masculino": int(lista[1])
        }

    print("Casos por genero extraidos!")

    return f'''Casos por genero:
    Femenino: {objeto.get("femenino")}
    Masculino: {objeto.get("masculino")}'''
