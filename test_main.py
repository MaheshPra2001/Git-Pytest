import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        assert add(3,3) == 6
        assert add(4,4) == 8


# if expected Output and actual output is same then we will get the result as pass
# Assert is assertion funtion which checking
#Actual == expected
# if it matches test case passed

