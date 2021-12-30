import twitter
import json
import config
from requests_oauthlib import OAuth1Session
import time,calendar
import datetime
import re
import sys
# assign the values accordingly
consumer_key=config.CONSUMER_KEY,
consumer_secret=config.CONSUMER_SECRET,
access_token_key=config.ACCESS_TOKEN,
access_token_secret=config.ACCESS_TOKEN_SECRET
  
# Authenticate Tweepy connection to Twitter API
api = twitter.Api(
    consumer_key=config.CONSUMER_KEY,
    consumer_secret=config.CONSUMER_SECRET,
    access_token_key=config.ACCESS_TOKEN,
    access_token_secret=config.ACCESS_TOKEN_SECRET
    #sleep_on_rate_limit=True
)

print("Enter the screen name.")
screen_name=input()

x=api.GetFriends(screen_name=screen_name,include_user_entities=True)

# print(vars(x))
f = open("./friends/"+str(screen_name)+'\'s_friends.txt', 'w')
print(str(screen_name)+"'s friends",file=f)
for i in x:
    print(i.name,i.screen_name,file=f)
    print(i.description,file=f)
f.close()

