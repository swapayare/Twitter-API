import requests_oauthlib
import json
import requests

from requests_oauthlib import OAuth1

search='imVkohli'

cousumer_key='c5dmNK5yspOHFGCLK6jJue9SO'
consumer_secret='dWZUjJo39KUz7jmaX5uibEnbIxud2c21rn5abO569Metb6pIvV'

auth=OAuth1(cousumer_key,consumer_secret)

url='https://stream.twitter.com/1.1/statuses/filter.json?track='+search

ans=requests.get(url,auth=auth)

data=ans.json()

print(data)
