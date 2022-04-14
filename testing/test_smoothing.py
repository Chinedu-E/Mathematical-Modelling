from Code.smoothing import Interpolation as ip
import unittest
import numpy as np
from numpy import array


class TestInterpolation(unittest.TestCase):
    def test_polycoefficients1(self):
        x = array([1.3, 1.7, 2.1])
        y = array([3.2, 4.4, 5.2])
        result  = ip.three_point_interpolation(x, y)
        exp = [-1.25, 6.75, -3.4625]
        self.assertEqual(result, exp)
        
        
    def test_polycoefficients2(self):
        x = array([0,1,2,3])
        y = array([1, -1, -3, 1])
        result  = ip.four_point_interpolation(x, y)
        exp = [1, -3, 0 , 1]
        self.assertEqual(result, exp)
        
        
    def test_polyorder1(self):
        x = array([0,1,3,4,7])
        y = array([1, 3, 49, 129, 813])
        result = ip.polynomial_order(x, y)
        exp = 3
        self.assertEqual(result, exp)
        
        
    def test_polyorder2(self):
        x = array([1,2,3,4,5,6,7])
        y = array([-5, -24, -27, 64, 375, 1080, 2401])
        result = ip.polynomial_order(x, y)
        exp = 4
        self.assertEqual(result, exp)
    
    
    def test_polyorder3(self):
        x = array([2,3,4,5, 6, 7,8, 10])
        y = array([40, 189, 576, 1375, 2808, 5145, 8704, 21000])
        result = ip.polynomial_order(x, y)
        exp = 4
        self.assertEqual(result, exp)
    
    
    def test_low_order_polynomial1(self):
        x = array([0,1,3,4,7])
        y = array([1, 3, 49, 129, 813])
        result = ip.low_order_polynomial(x, y)
        exp = [3, -5, 4, 1]
        self.assertEqual(result, exp)
        
        
    def test_low_order_polynomial2(self):
        x = array([2,3,4,5, 6, 7,8, 10])
        y = array([40, 189, 576, 1375, 2808, 5145, 8704, 21000])
        result = ip.low_order_polynomial(x, y)
        exp = [2, 1, 0, 0, 0]
        self.assertEqual(result, exp)
        
if __name__ == '__main__':
    unittest.main()