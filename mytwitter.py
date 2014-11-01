# -*- coding: utf-8 -*-

import requests as req
from requests_oauthlib import OAuth1

api_key = "" 
api_secret = ""  
token = "" 
token_secret = ""

auth = OAuth1(api_key, api_secret, token, token_secret)

url = "https://api.twitter.com/1.1/statuses/update.json"

def myUpdate_status(post_str):
    data = {"status":post_str}
    res = req.post(url,data=data,auth=auth)
