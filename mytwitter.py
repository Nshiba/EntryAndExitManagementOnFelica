# -*- coding: utf-8 -*-

import requests as req
from requests_oauthlib import OAuth1

api_key = 'VVeTWB7z2tnOjSGRqNmJQVEPE'
api_secret = 'VKjmZloi2RYam7ioeN4O5Wa67DZEp2zLbUm6ykrxbnor04xrrE'
token = '2819411641-IdNCtvx2gY5AxRidHVhPUhck330EDu0iE97nZow'
token_secret = 'LmgFcdXcrIaTGL3NVpiDOSxOGrW5puxnkwyde0LfWIN8B'

auth = OAuth1(api_key, api_secret, token, token_secret)

url = "https://api.twitter.com/1.1/statuses/update.json"

def myUpdate_status(post_str):
    data = {"status":post_str}
    res = req.post(url,data=data,auth=auth)
