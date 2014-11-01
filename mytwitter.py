# -*- coding: utf-8 -*-

import requests as req
from requests_oauthlib import OAuth1

api_key = "v9nCQxM4HxqQNIBzNfPH4Ex2V" 
api_secret = "QLifWZUrlmzaqKkdwOeZlTgYkqD3DfVdJZ7c10erKvTMn24sWn"  
token = "2206303868-nQaHYODrMPmra1RPNaiZv35N9TTDKLSMUxqipUP" 
token_secret = "PjnL1mKP8DXhAnCC9VO6TIYwtrnUkDx7lMTSHSt7BX4fH"

auth = OAuth1(api_key, api_secret, token, token_secret)

url = "https://api.twitter.com/1.1/statuses/update.json"

def myUpdate_status(post_str):
    data = {"status":post_str}
    res = req.post(url,data=data,auth=auth)
