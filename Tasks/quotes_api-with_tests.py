import requests
import json
import sys

req = requests.get('http://quotes.rest/qod.json?category=inspire') #quotes
#req = requests.get('http://quotes.rest/bible/verse.json?book=3') #bibleverse
#if req.status_code != 200:
#	sys.exit('Interrupted.. request is-not 200')
req=req.json()
print(json.dumps(req,indent=4))
#import ipdb; ipdb.set_trace()

quote = req['contents']['quotes'][0]['quote']
author = req['contents']['quotes'][0]['author']
tags = req['contents']['quotes'][0]['tags']


print(":: Quote of the Day ::")
print('"' + quote + '"')
print('Author : ' + author)
print('Tags : ')
for d in tags:
	print(d + ',')
