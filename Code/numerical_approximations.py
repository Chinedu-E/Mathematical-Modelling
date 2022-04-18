from fractions import Fraction
from typing import Callable

import pandas as pd


class NumericalApproximation:
    @classmethod
    def range_kutta_formula(cls,func: Callable[[float, float], float],
                      step_size: float,
                      x: float, y: float) -> list[float]:
        '''The Runge-Kutta Method of 4th order '''
        k1 = step_size * func(x, y)
        k2 = step_size * func(x + 0.5*step_size, y + 0.5*k1)
        k3 = step_size * func(x + 0.5*step_size, y + 0.5*k2)
        k4 = step_size * func(x + step_size, y + k3)
        return [k1, k2, k3, k4]

    @classmethod
    def euler_formula(cls,func: Callable[[float, float], float],
                      step_size: float,
                      x: float, y: float) -> float:
            return y + step_size * func(x, y)

    
    @staticmethod
    def eulers_method(func: Callable[[float, float], float],
                      initial_values: tuple[float, float],
                      step_size: float,
                      target: float) -> pd.DataFrame:
        x_s = [initial_values[0]]
        y_s = [initial_values[1]]
        
        for i in range(50):
            y = NumericalApproximation.euler_formula(func, step_size, x_s[i], y_s[i])
            y_s.append(y)
            next_step = x_s[i] + step_size
            x_s.append(next_step)
            if next_step == target:
                break
        
        table = pd.DataFrame()
        table['x'] = x_s
        table['y'] = y_s
        return table
    
    
    @staticmethod
    def eulers_system():
        pass
    
    
    @staticmethod
    def eulers_method_improved(func: Callable[[float, float], float],
                      initial_values: tuple[float, float],
                      step_size: float,
                      target: float) -> pd.DataFrame:
        x_s = [initial_values[0]]
        y_predictor = [initial_values[1]] 
        y_corrector = [initial_values[1]] 
        formula = NumericalApproximation.euler_formula
        for i in range(50):
            y_p = formula(func, step_size, x_s[i], y_corrector[i])
            y_predictor.append(y_p)
            next_step = x_s[i] + step_size
            x_s.append(next_step)
            y_c = y_corrector[i] + (0.5 * step_size * (func(x_s[i], y_corrector[i]) + func(x_s[i+1], y_predictor[i+1])))
            y_corrector.append(y_c)
            if next_step == target:
                break
        table = pd.DataFrame()
        table['x'] = x_s
        table['y_predictor'] = y_predictor
        table['y_corrector'] = y_corrector
        return table
    
    
    @staticmethod
    def range_kutta_method(func: Callable[[float, float], float],
                      initial_values: tuple[float, float],
                      step_size: float,
                      target: float) -> pd.DataFrame:
        '''The Runge-Kutta Method of 4th order '''
        x_s = [initial_values[0]]
        y_s = [initial_values[1]]
        k1, k2, k3, k4 = [], [], [], []
        formula = NumericalApproximation.range_kutta_formula
        iter_length = int(target/step_size)
        for i in range(iter_length):
            k: list[float] = formula(func, step_size, x_s[i], y_s[i])
            k1.append(k[0])
            k2.append(k[1])
            k3.append(k[2])
            k4.append(k[3])
            y = y_s[i] + (Fraction(1, 6) * (k[0]+ 2*k[1]+ 2*k[2]+ k[3]))
            y_s.append(y)
            next_step = x_s[i] + step_size
            x_s.append(next_step)
            if next_step == target:
                break
        k1.append(0)
        k2.append(0)
        k3.append(0)
        k4.append(0)
        table = pd.DataFrame()
        table['x'] = x_s
        table['y'] = y_s 
        table['k1'] = k1 
        table['k2'] = k2
        table['k3'] = k3
        table['k4'] = k4
        return table

if __name__ == '__main__':
    f = lambda x, y: x+y
    initial_values = (0, 0)
    table = NumericalApproximation.eulers_method_improved(f, initial_values, 0.1, 0.4)
    print(table)
    