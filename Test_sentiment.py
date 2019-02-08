import requests_oauthlib
import json
import requests

from requests_oauthlib import OAuth1
from textblob import TextBlob

search='python'

cousumer_key='c5dmNK5yspOHFGCLK6jJue9SO'
consumer_secret='dWZUjJo39KUz7jmaX5uibEnbIxud2c21rn5abO569Metb6pIvV'

auth=OAuth1(cousumer_key,consumer_secret)

url='https://api.twitter.com/1.1/search/tweets.json?q='+search

ans=requests.get(url,auth=auth)

data=ans.json()
test=TextBlob(str(data))


print(test.sentiment)
