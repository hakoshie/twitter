#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import config
from requests_oauthlib import OAuth1Session
import time,calendar
import datetime
import re
import sys
# OAuth認証部分
CK      = config.CONSUMER_KEY
CS      = config.CONSUMER_SECRET
AT      = config.ACCESS_TOKEN
ATS     = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

# Twitter Endpoint(ユーザータイムラインを取得する)
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

# Enedpointへ渡すパラメーター
params ={
         'count'       : 5,             # 取得するtweet数
           # twitterアカウント名
        }
def last_unixtime():
    params['screen_name']=config.MAIN_SCREEN_NAME
    req = twitter.get(url, params = params)
    if req.status_code == 200:
        res = json.loads(req.text)
        for i,tweet in enumerate(res): 
            time_utc = time.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
            unix_time = calendar.timegm(time_utc)
            if(i==0):
                return unix_time
    else:
        print("Failed: %d" % req.status_code)
def main(): 
    print("insert screen name")
    print(">>> ",end='')
    params['screen_name']=input()         
    print("fill in the max number")
    print(">>> ",end='') 
    import re
    a=input()
    re.sub(r"\D","",a)
    if(len(a)==0):
        a=5
    params['count']=int(a)    
    print(params)

    req = twitter.get(url, params = params)
    if req.status_code == 200:
            res = json.loads(req.text)
            for tweet in res: 
                time_utc = time.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
                unix_time = calendar.timegm(time_utc)
                time_local = time.localtime(unix_time)
                japan_time = time.strftime("%Y-%m-%d %a %H:%M:%S", time_local)
                print(tweet['user']['name'],'@'+tweet['user']['screen_name'],'::')
                print(" "+tweet['text'])
                print(" RT",tweet['retweet_count'],"Fav",tweet['favorite_count'])
                client=tweet['source']
                client=re.sub(r"<[^>]*?>","",client)
                #print(tweet['created_at'])
            
                print(japan_time,client)
                print('*******************************************')
    else:
            print("Failed: %d" % req.status_code)
if __name__ == "__main__":
    main()