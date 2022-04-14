from typing import Callable, Iterable
import pandas as pd
from scipy.integrate import fixed_quad,quad
import numpy as np
import math
        
class Integrals:
    def __str__(self):
        return "Integrals"
    
    @staticmethod
    def guassian_quadrature(n: int, a: int, b: int, f: Callable[[float], float]):
        return fixed_quad(f, a=a, b=b,n=n)
    
    @staticmethod
    def true_value(a,b,f) -> float:
        return quad(f, a, b)[0]  
    
    @staticmethod
    def simprule(n: int, a: int, b: int, f: Callable[[float], float]) -> tuple[float, float]:
        h = (b-a)/n
        x = [a + i*h for i in range(n+1)]
        iter = []
        n = n+1
        for i in range(n):
            if i in (0,n-1):
                simp = f(x[i])
                iter.append(simp)
            elif i%2 == 1:
                simp = 4*f(x[i])
                iter.append(simp)
            elif i%2 == 0:
                simp = 2*f(x[i])
                iter.append(simp)
        simpr = (h/3)* math.fsum(iter)
        exact = quad(f, a, b)[0]
        error = exact - simpr
        return (simpr, error)
    
    @staticmethod
    def traprule(n: int, a: int, b: int, f: Callable[[float], float]) -> tuple[float, float]:
        h = (b-a)/n
        x = [a + i*h for i in range(n+1)]
        iter = []
        n = n+1
        for i in range(n):
            if i in (0,n-1):
                trap = f(x[i])
                iter.append(trap)
            else:
                trap = 2*f(x[i])
                iter.append(trap)
        trapr = (h/2)* math.fsum(iter)
        exact = quad(f, a, b)[0]
        error = exact - trapr
        return (trapr, error)
    
    @staticmethod
    def midrule(n: int, a: int, b: int, f: Callable[[float], float]) -> tuple[float, float]:
        h = (b-a)/n
        x = [a + i*h for i in range(n+1)]
        iter = []
        for i in range(n):
            mid = (x[i]+x[i+1])/2
            iter.append(f(mid))
        midr = h*math.fsum(iter)
        exact = quad(f, a, b)[0]
        error = exact - midr
        return (midr, error)
    
    @staticmethod
    def monte_carlo_integration(random_numbers: Iterable, a: int, b: int, f: Callable[[float], float]) -> float:
        n = len(random_numbers) 
        x = random_numbers
        summate = []
        h = (b-a)/n
        for i in range(n):
            summate.append(f(x[i]))
        summ = sum(summate)
        return summ*h
    
     

