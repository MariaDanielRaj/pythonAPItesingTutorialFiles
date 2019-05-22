import requests
import json
import sys
import pytest
import unittest

class APICalls(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		print('Starting Up the APIClass Program ....')
	
	@classmethod	
	def tearDownClass(cls):
		print('Tearing Down the APIClass Program .... DONE !')
		
	@pytest.mark.run(order=1)
	def requestAPI(self):
		req = requests.get('http://quotes.rest/qod.json?category=inspire') #quotes
		#req = requests.get('http://quotes.rest/bible/verse.json?book=3') #bibleverse
		if req.status_code != 200:
			return 0
		return req
		
	@pytest.mark.dependency()
	def printJson(self):
		request = requestAPI()
		if request is false:
			sys.exit('Interrupted.. request is-not 200')
		request=reqest.json()
		print(json.dumps(request,indent=4))
		
	
	@pytest.mark.dependency(depends=['APICalls::printJSON'])
	def printQuote(self):
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
