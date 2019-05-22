
import pytest

test_data = [[1,2,2],
[2,4,8],
[3,3,9]]

setup = 1

def setup():
	print(".. THIS IS SETUP")
	setup = 0

@pytest.mark.parametrize("a, b, c", test_data)
def test_mul(a,b,c):
	if setup:
		setup()
	assert a*b == c
