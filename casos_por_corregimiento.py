from bs4 import BeautifulSoup
import datetime
import csv

now = datetime.datetime.now()
dia_de_hoy = f"{now.day}/{now.month}/{now.year}"


def obtener_casos_por_corregimiento():

    print("Extrayendo casos por corregimiento")

    pagina = open("./output/casos_por_corregimiento.html")

    with pagina as markup:
        soup = BeautifulSoup(markup.read(), "html.parser")

        lista = []

        for tag in soup.findAll("p"):
            lista.append(tag.text.strip())

        lista = lista[1:-1]

        corregimientos = list(map(lambda algunTexto: algunTexto.title(), lista[0:-1:2]))
        total_arreglado = list(
            map(
                lambda algunTexto: algunTexto.replace("Casos confirmados:\xa0", ""),
                lista[1:-1:2],
            )
        )

        nueva_lista = []

        indice = 0
        for corregimiento in corregimientos:
            objeto = {
                "corregimiento": corregimiento,
                "casos_confirmados": int(total_arreglado[indice]),
                "fecha": dia_de_hoy,
            }
            nueva_lista.append(objeto)
            indice += 1

        def actualizar_base_de_datos(lista):
            with open(
                f"./output/base_de_datos/base_de_datos_corregimientos.csv",
                "a",
                newline="",
            ) as csvfile:
                fieldnames = ["corregimiento", "casos_confirmados", "fecha"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for row in lista:
                    writer.writerow(row)

            return "Lista completa"

        actualizar_base_de_datos(nueva_lista)

        print("Casos por corregimiento extraidos!")

        def crear_lista_de_corregimientos(lista):
            string = "\n"
            for corregimiento in lista:
                string += f"""{corregimiento.get('corregimiento')} : {corregimiento.get('casos_confirmados')}\n"""
            return string

        def crear_lista_de_tweets(lista_grande):
            conteo = 1
            lista_de_tweets = []
            for lista in chunks:
                lista_de_tweets.append(
                    f"""Casos Confirmados por Corregimiento ({conteo}/{len(chunks)}){crear_lista_de_corregimientos(lista)}#COVID19 #COVIDー19 #Panama"""
                )
                conteo += 1
            return lista_de_tweets

        chunks = [nueva_lista[x : x + 10] for x in range(0, len(nueva_lista), 10)]

        return crear_lista_de_tweets(chunks)
