from bs4 import BeautifulSoup


def obtener_casos_principales():
    print("Obteniendo casos principales!")
    pagina = open("./output/casos.html")

    with pagina as markup:
        soup = BeautifulSoup(markup.read(), "html.parser")

        lista = []

        for tag in soup.findAll("text"):
            lista.append(tag.text.strip())

        valores = list(map(int, lista[1::2]))

        objeto = {
            'activos': sum(valores)-(valores[2]+valores[0]),
            'recuperados': valores[0],
            'hospitalizados': valores[1],
            'fallecidos': valores[2],
            'aislamiento': valores[3],
            "uci": valores[-1],
            'total': sum(valores)
        }


    print("Casos principales extraidos con exito!")

    tweet = f'''Casos de COVID-19 en Panamá
        
Casos: {objeto.get("total")} - Activos: {objeto.get("activos")}
Hospitalizados: {objeto.get("hospitalizados")} - UCI: {objeto.get("uci")}
Fallecidos: {objeto.get("fallecidos")} - Recuperados: {objeto.get("recuperados")}
Aislamiento: {objeto.get("aislamiento")}

Actualizado cada 24 horas
#Coronavirus #COVID19 #COVIDー19 #Panamá #ProtegetePanama #QuedateenCasa
Fuente: MINSA https://bit.ly/3bDYxIV'''

    return tweet
