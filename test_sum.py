
import unittest

import my_tool

class TestSum(unittest.TestCase):
    def test_sum1(self):
        result = my_tool.sum(10, 20)
        self.assertEqual(result, 30)
        
    def test_sum2(self):
        result = my_tool.sum(0, 0)
        self.assertEqual(result,0)
    
    def test_sum3(self):
        result = my_tool.sum(0, -1)
        self.assertEqual(result,1)
