import unittest
import numpy as np     
import pandas as pd
from Code.numerical_approximations import NumericalApproximation

class TestNumericalApproximations(unittest.TestCase):
    
    def test_eulers_method(self):
        f = lambda x,y: x + y
        na = NumericalApproximation
        res = na.eulers_method(f, (0, 0), 0.1, 0.4)
        result = round(res['y'].values[-1], 4)
        exp = 0.0641
        self.assertEqual(result, exp)
    
    
    def test_eulers_method_improved(self):
        f = lambda x,y: x + y
        na = NumericalApproximation
        res = na.eulers_method_improved(f, (0, 0), 0.1, 0.4)
        result = round(res["y_corrector"].values[-1], 4)
        exp = 0.0909
        self.assertEqual(result, exp)
    
    
    def test_range_kutta_method1(self):
        f = lambda x,y: x + y
        na = NumericalApproximation
        res = na.range_kutta_method(f, (0, 0), 0.1, 0.4)
        result = round(res['y'].values[-1], 4)
        exp = 0.0918
        self.assertEqual(result, exp)
        
        
    def test_range_kutta_method2(self):
        f = lambda x, y: y - (x**2) + 1
        na = NumericalApproximation
        res = na.range_kutta_method(f, (0, 0.5), 0.5, 2)
        result = round(res['y'].values[-1], 4)
        exp = 5.3016
        self.assertEqual(result, exp)
        
           
    def test_range_kutta_method3(self):
        f = lambda x, y: y - (x**2) + 1
        na = NumericalApproximation
        res = na.range_kutta_method(f, (0, 0.5), 0.2, 2)
        result = round(res['y'].values[-1], 4)
        exp = 5.3054
        self.assertEqual(result, exp)
        
        
    def test_range_kutta_method4(self):
        f = lambda x, y: (5*(x**2) - y)* np.exp(-x-y)
        na = NumericalApproximation
        res = na.range_kutta_method(f, (0, 1), 0.1, 1)
        result = round(res['y'].values[-1], 4)
        exp = 1.0716
        self.assertEqual(result, exp)
    
    
 
    
if __name__ == "__main__":
    unittest.main()