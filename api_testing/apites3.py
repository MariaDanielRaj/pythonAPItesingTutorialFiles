import requests
import json
import oauth2
#import key


consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth2.Token(key=key, secret=secret)
client = oauth2.Client(consumer, token)
timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
resp, content = client.request(timeline_endpoint)

tweets = json.loads(content)

for tweet in tweets:
	print(tweet['text'])
	print("*"*100)
