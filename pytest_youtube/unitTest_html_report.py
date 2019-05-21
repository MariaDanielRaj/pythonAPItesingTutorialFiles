import unittest

class test1(unittest.TestCase):
		@classmethod
		def setUpClass(cls):
			print('..this is set up class')

		@classmethod
		def tearDownClass(cls):
			print('..this is tear down class')
			
				
		def setup(self):
			print('setup')
		def tearDown(self):
			print('tearDown')
		def test1(self):
			print('test1')
		def test2(self):
			print('test2')
			
