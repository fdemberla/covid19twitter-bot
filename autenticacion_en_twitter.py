import tweepy
from tweepy import TweepError
from api_Keys import api_keys

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_keys.get("API_1"), api_keys.get("API_2"))
auth.set_access_token(api_keys.get("API_TOKEN_1"), api_keys.get("API_TOKEN_2"))

api = tweepy.API(auth)


def autenticar():

    try:
        api.verify_credentials()
        print("Credenciales verificadas!")
    except TweepError as error:
        print("Error en autenticacion!")
        print(error.reason)

    return api
