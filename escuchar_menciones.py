import tweepy
import json
from tweepy import TweepError
from api_Keys import api_keys

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_keys.get("API_1"), api_keys.get("API_2"))
auth.set_access_token(api_keys.get("API_TOKEN_1"), api_keys.get("API_TOKEN_2"))

api = tweepy.API(auth)

corregimientos = json.load(open("./output/corregimientos.txt"))

menciones = api.mentions_timeline()

tweets_atendidos = []


def encontrar_corregimiento(mencion):
    if "corregimiento" in mencion._json.get("text"):
        return mencion


def verificar_con_lista(text):

    for corregimiento in corregimientos:
        if (
            text.split("corregimiento".lower(), 1)[1].title()
            in corregimiento.get("corregimiento").lower()
        ):
            tweets_atendidos.append(corregimiento.get("id"))
            return corregimiento


menciones_con_palabra_corregimiento = list(filter(encontrar_corregimiento, menciones))

menciones_filtradas = [
    {
        "id": i._json.get("id"),
        "text": i._json.get("text"),
        "user": i._json.get("user").get("screen_name"),
    }
    for i in menciones_con_palabra_corregimiento
]

for mencion in menciones_filtradas:
    print(verificar_con_lista(mencion.get("text")))


# if len(menciones_con_palabra_corregimiento) > 0:
#     for mencion in menciones_con_palabra_corregimiento:
#         print(mencion._json.get("text"))

#     api.update_status(
#         f"Hola @{tweet._json.get('user').get('screen_name')}", tweet._json.get("id")
#     )
