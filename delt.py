# pip install python-twitter 
import twitter 
import json
import config
import time ,calendar
import re

issub="n"
screen_name=config.MAIN_SCREEN_NAME
api = twitter.Api(
    consumer_key=config.CONSUMER_KEY,
    consumer_secret=config.CONSUMER_SECRET,
    access_token_key=config.ACCESS_TOKEN,
    access_token_secret=config.ACCESS_TOKEN_SECRET,
    sleep_on_rate_limit=True
)
if(issub=='y'):
    api = twitter.Api(
    consumer_key=config.CONSUMER_KEY,
    consumer_secret=config.CONSUMER_SECRET,
    access_token_key=config.OAUTH_TOKEN,
    access_token_secret=config.OAUTH_TOKEN_SECRET
    )
    screen_name=config.SUB_SCREEN_NAME

cnt="100"

if(re.search(r'\d',cnt)):
    cnt=int(cnt)
else:
    cnt=3200

while True:
    statuses = api.GetUserTimeline(screen_name=screen_name,count=cnt)
    if(len(statuses)):
        print("----------------deleted tweets----------------")
    else :
        print("there are no tweets")
    for i,s in enumerate(statuses):
        print(s.user.name,'@'+s.user.screen_name)
        print(s.text)
        time_utc = time.strptime(s.created_at, '%a %b %d %H:%M:%S +0000 %Y')
        unix_time = calendar.timegm(time_utc)
        time_local = time.localtime(unix_time)
        japan_time = time.strftime("%Y-%m-%d %a %H:%M:%S", time_local)
        print(japan_time)
        try:
            #if(i!=0):            
            api.DestroyStatus(s.id)
        except:
            print("error")
    break