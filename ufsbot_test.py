#!/usr/bin/env python3
#coding: utf-8

import tweepy
import json
import urllib
import ruscrap

CONSUMER_KEY = '5P65CgU64yu4DyoEdDwXZlJsm'
CONSUMER_SECRET = '0pm3nOe4yUGOubdonhxupkfAbQwCDfPTsObiVKY0pX311xFZMI'
ACCESS_KEY = '4865224378-YuiT8hRPOUHg1BMAjX376v4TI2k8TQccVdgzUws'
ACCESS_SECRET = 'TzIRRqkzcE5a9cDwbxE1us1ErqQNQNXOENKCFsGEcGiSp'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def gerar_gif():
    url = 'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=food+anime'
    response = urllib.request.urlopen(url)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    urllib.request.urlretrieve(json_obj['data']['image_original_url'], 'meu.gif')

gerar_gif()
filename = open('meu.gif', 'rb')

cardapio = ruscrap.cardapio_hoje()
api.update_with_media('meu.gif',status=cardapio)
