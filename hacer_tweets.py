import tweepy
import time
from tweepy import TweepError

from autenticacion_en_twitter import autenticar

# importar scripts
from extraer_datos import extractor_de_datos
from casos_principales import obtener_casos_principales
from casos_por_genero import obtener_casos_por_genero
from pruebas_realizadas import obtener_pruebas_realizadas

from casos_por_corregimiento import obtener_casos_por_corregimiento
from rango_de_edades import obtener_rango_de_edades

api = autenticar()

usuario = api.get_user("@fdemberla")

try:
    # Enviarme un mensaje cuando inicia el bot.
    api.send_direct_message(usuario._json.get("id"), "Hola! Iniciando script!")

    print("Extrayendo datos de la pagina web!")
    extractor_de_datos()
    datos = obtener_casos_principales()
    pruebas = obtener_pruebas_realizadas()
    genero = obtener_casos_por_genero()
    rango_de_edades = obtener_rango_de_edades()
    lista_de_tweets = [datos, genero, rango_de_edades, pruebas]
    corregimientos = obtener_casos_por_corregimiento()
    print("Haciendo tweets!")
    #    Hacer tweets
    cantidad_de_tweets = 0
    tweet_id_anterior = ""
    for tweet in lista_de_tweets:
        cantidad_de_tweets += 1
        tweet_actual = api.update_status(
            tweet, in_reply_to_status_id=tweet_id_anterior, username="@PanamaCovid19"
        )
        tweet_id_anterior = tweet_actual._json.get("id")
        time.sleep(1)

        # casos por corregimiento.

    time.sleep(10)

    for tweet in corregimientos:
        cantidad_de_tweets += 1
        tweet_corregimiento = api.update_status(
            tweet, in_reply_to_status_id=tweet_id_anterior, username="@PanamaCovid19",
        )
        tweet_id_anterior = tweet_corregimiento._json.get("id")
        time.sleep(3)
    print("Tweets enviados con exito!")

    # Enviarme un mensaje cuando se completa el script
    api.send_direct_message(
        usuario._json.get("id"),
        f"Script finalizado, {cantidad_de_tweets} tweets hechos. Hasta luego! ",
    )

except TweepError as error:
    print(error.reason)
    print(error.response)
    # Enviarme un mensaje si el bot falla.
    api.send_direct_message(
        usuario._json.get("id"),
        f"Hola, algo ha salido mal con el script, razon: {error.reason}",
    )
