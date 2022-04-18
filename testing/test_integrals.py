import unittest
from math import sin
import numpy as np
from Code.integrate import Integrals
from Code.Randomnum import RNG


class TestIntegrals(unittest.TestCase):
    def test_truevalue(self):
        f = lambda x: 1/(1 + np.exp(x))
        result = round(Integrals.true_value(0, 2, f), 5)
        exp = 0.56622
        self.assertEqual(result, exp)
        
        
    def test_simprule1(self):
        f = lambda x: sin(x**2)
        result = round(Integrals.simprule(4, 0, 2, f)[0], 4)
        exp = 0.83800
        self.assertEqual(result, exp)
        
        
    def test_simprule2(self):
        f = lambda x: 1/(1 + np.exp(x))
        result = round(Integrals.simprule(4, 0, 2, f)[0], 5)
        exp = 0.56616
        self.assertEqual(result, exp)
        
        
    def test_simprule3(self):
        f = lambda x: np.log(x**2 + 3)
        result = round(Integrals.simprule(4, 0, 4, f)[0], 4)
        exp = 	7.8066
        self.assertEqual(result, exp)
        
        
    def test_midrule(self):
        f = lambda x: sin(x**2)
        result = round(Integrals.midrule(4, 0, 2, f)[0], 5)
        exp = 0.83737
        self.assertEqual(result, exp)
        
        
    def test_traprule(self):
        f = lambda x: sin(x**2)
        result = round(Integrals.traprule(4, 0, 2, f)[0], 5)
        exp = 0.74427
        self.assertEqual(result, exp)
        
        
    def test_guassianrule1(self):
        f = lambda x: np.sin(x)**2
        result = round(Integrals.guassian_quadrature(4, 0, 1, f)[0],5)
        exp = 0.27268
        self.assertEqual(result, exp)
        

    def test_guassianrule2(self):
        f = lambda x: np.sin(x)
        result = round(Integrals.guassian_quadrature(2, 0, 1.2, f)[0],5)
        exp = 0.63732
        self.assertEqual(result, exp)

    
    def test_monte_carlo_integration1(self):
        f = lambda x: np.log(1+x**2)
        rand_nums: list[float] = RNG.middle_square(10, 7613, as_decimal= True)
        result = Integrals.monte_carlo_integration(rand_nums, 0, 1, f)
        exp = 0.27694
        self.assertEqual(round(result, 5), exp)
    
if __name__ == '__main__':
    unittest.main()