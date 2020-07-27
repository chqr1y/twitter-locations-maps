#!/usr/bin/env python3

import tweepy
import json

CONSUMER_KEY = 'YOUR OWN CONSUMER KEY'
CONSUMER_SECRET = 'YOU OWN CONSUMER SECRET'
output_file = 'twitter_available_locations.json'

auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)
r = api.trends_available()

f = open(output_file, 'w')
f.write(json.dumps(r))

print(f"Success : all twitter available locations for twitter trends have been written in {output_file}")
