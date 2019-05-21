import unittest
import pytest


class test2(unittest.TestCase):
	@pytest.mark.last
	def testa(self):
		pass
	@pytest.mark.run(order=4)
	def testd(self):
		pass
	@pytest.mark.first
	def testb(self):
		pass
	@pytest.mark.run(order=3)
	def testc(self):
		pass
