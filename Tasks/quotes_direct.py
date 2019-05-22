import requests
import json
import sys
import pytest
import unittest

class APICalls(unittest.TestCase):

	@pytest.mark.dependency(depends=['APICalls::test_requestAPI'])
	def test_printE(self):
		print('......ENDED......')
		
	@pytest.mark.first	
	def test_printS(self):
		print('......STARTED......')

	
	@pytest.mark.dependency()
	@pytest.mark.run(order=1)
	def test_requestAPI(self):
		req = requests.get('http://quotes.rest/qod.json?category=inspire') #quotes
		if req.status_code != 200:
			request = 0
		else:
			request = req
		if request == 0:
			sys.exit('Interrupted.. request is-not 200')
		request=request.json()
		print(json.dumps(request,indent=4))
		#import ipdb; ipdb.set_trace()
		quote = request['contents']['quotes'][0]['quote']
		author = request['contents']['quotes'][0]['author']
		tags = request['contents']['quotes'][0]['tags']

		print('*'*50 + " Quote of the Day " + '*'*50)
		print('Quote : "' + quote + '"')
		print('Author : ' + author)
		print('Tags : ' + str(tags))
