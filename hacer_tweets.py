import tweepy
import time

# importar scripts
from extraer_datos import extractor_de_datos
from casos_principales import obtener_casos_principales
from casos_por_genero import obtener_casos_por_genero
from pruebas_realizadas import obtener_pruebas_realizadas
from casos_por_corregimiento import obtener_casos_por_corregimiento
from rango_de_edades import obtener_rango_de_edades

#import keys
from api_Keys import api_keys

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_keys.get("API_1"),
                           api_keys.get("API_2"))
auth.set_access_token(api_keys.get("API_TOKEN_1"),
                      api_keys.get("API_TOKEN_2"))

api = tweepy.API(auth)

try:
    print("Extrayendo datos de la pagina web!")
    extractor_de_datos()
    datos = obtener_casos_principales()
    pruebas = obtener_pruebas_realizadas()
    genero = obtener_casos_por_genero()
    rango_de_edades = obtener_rango_de_edades()
    lista_de_tweets = [datos, pruebas, genero, rango_de_edades]
    corregimientos = obtener_casos_por_corregimiento()
    print("Haciendo tweets!")
   # Hacer tweets
    for tweet in lista_de_tweets:
            api.update_status(tweet)
            time.sleep(1)

        # casos por corregimiento.
    for tweet in corregimientos:
            api.update_status(tweet)
            time.sleep(1)
    print("Tweets enviados con exito!")
except:
    print(f"Algo salio mal!")
