
import unittest
import pytest


class test2(unittest.TestCase):
	
	@pytest.mark.dependency(depends=['test2::testc'])
	def testa(self):
		pass
	@pytest.mark.dependency()
	def testd(self):
		pass
	@pytest.mark.dependency()
	def testb(self):
		pass
	
	@pytest.mark.run(order=1)
	@pytest.mark.dependency()
	def testc(self):
		assert false
