import twitter
import json
import config
from requests_oauthlib import OAuth1Session
import time,calendar
import datetime
import re
import sys

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

x=api.GetFollowers(screen_name=screen_name)

# print(vars(x))
f = open("./followers/"+str(screen_name)+'\'s_followers.txt', 'w')
print(str(screen_name)+"'s followers",file=f)
for i in x:
    print(i.screen_name,file=f)
f.close()

