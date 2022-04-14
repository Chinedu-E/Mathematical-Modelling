from typing import Iterable
import pandas as pd
import numpy as np
import sympy as sym
from sympy import Poly

class Interpolation:
    def __call__(self, x: Iterable, y: Iterable) -> str:
        output = ""
        self.poly_order = self.polynomial_order(x,y)
        self.table = self.divided_difference_table(x,y,return_array=False)
        self.polynomial = self.low_order_polynomial(x,y, as_string=True)
        output += f"\nDatapoints entered is a {self.poly_order} order polynomial\n"
        output += f'low order polynomial of P(x) = {self.polynomial}\n\n'
        output += f'Divded difference table: \n'
        output += str(self.table)
        return output
    
    def __str__(self):
        return 'Interpolation'
        
    @staticmethod
    def _equal_checker(x: Iterable, y: Iterable) -> None:
        if len(x) != len(y):
            raise ValueError('length of x and y must be equal')
        return None
    
    @staticmethod
    def divided_difference_table(x: Iterable, y: Iterable, return_array: bool = True) -> list[list[int]]:
        Interpolation._equal_checker(x, y)
        n = len(x)
        table = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            table[i][0] = y[i] # filling the first column with given y values
        def _formula():
            try:
                for i in range(1, n): 
                    for j in range(n - i): 
                        table[j][i] = ((table[j][i - 1] - table[j + 1][i - 1]) /
                                             (x[j] - x[i + j]))
            except:
                pass
            return table
        table = _formula()
        if return_array:
            return table
        else:
            return pd.DataFrame(table)
        
    @staticmethod
    def three_point_interpolation(x: Iterable, y: Iterable, as_string: bool = False) -> list[float]:
        Interpolation._equal_checker(x, y)
        if len(x) != 3:
            raise ValueError('length of x and y must be 3')
        x_symbol = sym.Symbol('x') 
        l1 = (x_symbol-x[1])*(x_symbol-x[2])/((x[0]-x[2])*(x[0]-x[1]))
        l2 = (x_symbol-x[0])*(x_symbol-x[2])/((x[1]-x[2])*(x[1]-x[0]))
        l3 = (x_symbol-x[0])*(x_symbol-x[1])/((x[2]-x[1])*(x[2]-x[0]))
        polynomial = l1*y[0] + l2*y[1] + l3*y[2]
        polynomial = sym.expand(polynomial)
        coeffs = list(np.around(np.array(Poly(polynomial,x_symbol).all_coeffs()).astype(float),4)) # getting coefficients of 
        if as_string:
            return str(polynomial)
        else:
            return coeffs
        
    @staticmethod
    def four_point_interpolation(x: Iterable, y: Iterable, as_string: bool = False) -> list[float]:
        Interpolation._equal_checker(x, y)
        if len(x) != 4:
            raise ValueError('length of x and y must be 3')
        x_symbol = sym.Symbol('x') 
        l1 = ((x_symbol-x[1])*(x_symbol-x[2])*(x_symbol-x[3]))/((x[0]-x[1])*(x[0] -x[2])*(x[0] -x[3]))
        l2 = ((x_symbol-x[0])*(x_symbol-x[2])*(x_symbol-x[3]))/((x[1]-x[0])*(x[1] -x[2])*(x[1] -x[3]))
        l3 = ((x_symbol-x[0])*(x_symbol-x[1])*(x_symbol-x[3]))/((x[2]-x[0])*(x[2] -x[1])*(x[2] -x[3]))
        l4 = ((x_symbol-x[0])*(x_symbol-x[1])*(x_symbol-x[2]))/((x[3]-x[0])*(x[3] -x[1])*(x[3] -x[2]))
        polynomial = l1*y[0] + l2*y[1] + l3*y[2] + l4*y[3]
        polynomial = sym.expand(polynomial)
        coeffs = list(np.around(np.array(Poly(polynomial,x_symbol).all_coeffs()).astype(float),4))     
        if as_string:
            return str(polynomial)
        else:
            return coeffs
        
    @staticmethod
    def polynomial_order(x: Iterable, y: Iterable) -> int:
        Interpolation._equal_checker(x, y)
        max_length = 0
        n = len(x)
        table = Interpolation.divided_difference_table(x,y)
        for i in range(n):
            table[i] = [j for j in table[i] if j != 0] #removing zeros from all lists if any
        for i in range(n):
            length = len(table[i])
            if length > max_length:
                max_length = length
        return max_length-1
    
    @staticmethod
    def low_order_polynomial(x: Iterable, y: Iterable, as_string: bool = False) -> list[float]:
        Interpolation._equal_checker(x, y)
        table = Interpolation.divided_difference_table(x,y)
        x_symbol = sym.Symbol('x')
        product = 1
        poly = 0
        for i in range(len(table[0])): #building the polynomial
            if i == 0:
                poly += table[0][i]
            else:
                if i == 1:
                    product *= (x_symbol-x[i-1])
                    poly += table[0][i]*product
                else:
                    product *= (x_symbol-x[i-1])
                    poly += table[0][i]*product
        polynomial = sym.expand(poly)
        coeffs = list(np.around(np.array(Poly(polynomial,x_symbol).all_coeffs()).astype(float),4))
        if as_string:
            return str(polynomial)
        else:
            return coeffs
        
        
