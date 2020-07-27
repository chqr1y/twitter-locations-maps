# get available locations for twitter trends

get_available_locations_for_twitter_trends.py calls the twitter API for getting the locations that Twitter has trending topic information for (https://developer.twitter.com/en/docs/trends/locations-with-trending-topics/api-reference/get-trends-available).

## usage
1. Install the dependances
```bash
$python3 -m venv venv
$source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

1. Set your own Twitter API credentials (more information about Twitter API here : https://developer.twitter.com/en/docs/basics/getting-started)
```bash
$ head get_available_locations_for_twitter_trends.py 
#!/usr/bin/env python3

import tweepy
import json

CONSUMER_KEY = 'YOUR OWN CONSUMER KEY'
CONSUMER_SECRET = 'YOU OWN CONSUMER SECRET'
output_file = 'twitter_available_locations.json'

auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
```

1. Run

```bash
$ python3 get_available_locations_for_twitter_trends.py                                                            
Success : all twitter available locations for twitter trends have been written in available_locations.json
$ cat available_locations.json | jq '.[]' | head -n 40
{
  "name": "Worldwide",
  "placeType": {
    "code": 19,
    "name": "Supername"
  },
  "url": "http://where.yahooapis.com/v1/place/1",
  "parentid": 0,
  "country": "",
  "woeid": 1,
  "countryCode": null
}
{
  "name": "Winnipeg",
  "placeType": {
    "code": 7,
    "name": "Town"
  },
  "url": "http://where.yahooapis.com/v1/place/2972",
  "parentid": 23424775,
  "country": "Canada",
  "woeid": 2972,
  "countryCode": "CA"
}
{
  "name": "Ottawa",
  "placeType": {
    "code": 7,
    "name": "Town"
  },
  "url": "http://where.yahooapis.com/v1/place/3369",
  "parentid": 23424775,
  "country": "Canada",
  "woeid": 3369,
  "countryCode": "CA"
}
{
  "name": "Quebec",
  "placeType": {
    "code": 7,

``` 

## Filter twitter locations to get only countries
I use the command jq (https://www.npmjs.com/package/node-jq):
```bash
cat available_locations.json | jq 'map(. | select(.placeType.name=="Country"))' > available_locations_countries.json
```
