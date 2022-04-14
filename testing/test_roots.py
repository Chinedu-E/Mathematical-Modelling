from math import sin
from Code.roots import FixedPoint, NewtonMethod, SDE

import unittest


class TestRoots(unittest.TestCase):
    def test_fixedpoint_method1(self):
        f = lambda x: (5-x**3)/ 5
        result = FixedPoint.fixed_point(f, 0.75, 50)
        result = round(result, 6)
        exp = 0.86883
        self.assertEqual(result, exp)
        
        
    def test_fixedpoint_method2(self):
        f = lambda x: sin(x+2)/ 2
        result = FixedPoint.fixed_point(f, 0.5, 50)
        result = round(result, 4)
        exp = 0.3542
        self.assertEqual(result, exp)
        
        
    def test_newton_method1(self):
        f = lambda x: x**6 - 2
        result = NewtonMethod.newton_method(f, 1, 50)
        result = round(result, 4)
        exp = 1.1224
        self.assertEqual(result, exp)
        
        
    def test_newton_method2(self):
        f = lambda x: x**3 - x + 1
        result = NewtonMethod.newton_method(f, -1, 50)
        result = round(result, 4)
        exp = -1.3247
        self.assertEqual(result, exp)


    def test_newton_method3(self):
        f = lambda x: x**5 - 5*x + 2
        result = NewtonMethod.newton_method(f, 2, 50)
        result = round(result, 4)
        exp = 1.3719
        self.assertEqual(result, exp)
        
        
    def test_sde_equilibrium(self):
        result = SDE.equilibrium(*[1.2,0.001,0.6,0.002])
        exp = (200,200)
        self.assertEqual(result, exp)
        
        
    def test_sde_equilibrium2(self):
        result = SDE.equilibrium(*[1.2, 0.001, 1.3, -0.002])
        exp = (150, 200)
        self.assertEqual(result, exp)
        
        
    def test_sde_equilibrium3(self):
        result = SDE.equilibrium(*[1.2, 0.002, 0.6, 0.002])
        exp = (200, 100)
        self.assertEqual(result, exp)
   
   
    def test_sde_sensitivity_analysis(self):
        f = lambda x, y: 1.2*x - 0.002*x*y
        g = lambda x, y: 0.6*y + 0.002*y*x
        result = SDE.sensitivity_analysis(f, g, 40, init_values=(150, 50))
        result = (result[0][30], result[1][30])
        exp = (223, 5)
        self.assertEqual(result, exp)
   
   
   
   
        
if __name__ == '__main__':
    unittest.main()