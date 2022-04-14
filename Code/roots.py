from abc import ABC, abstractmethod
from scipy.misc import derivative
from typing import Callable, Iterable, Sequence, ClassVar, Union
import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.DataFrame

class Roots(ABC):
    values: ClassVar[list[Union[int, float]]] = []
    
    @abstractmethod
    def table(self) -> dataframe:
        return pd.DataFrame(self.values)
    
    @abstractmethod
    def plot_iterations(self):
        n = len(self.values)
        plt.plot([i for i in range(n)], self.values)
        plt.xlabel("Iterations")
        plt.ylabel("Root")
        plt.show()

class FixedPoint(Roots):

    def __str__(self):
        return "Fixed Point Iteration"
    
    def __call__(self, f: Callable[[float], float], initial_value: int, max_iter: int) -> str:
        self.root = FixedPoint.fixed_point(f, initial_value, max_iter)
        self.iter_table = self.table()
        return f"root converges at {self.root}\nTable:\n{str(self.iter_table)}"
        
    @staticmethod
    def fixed_point(f: Callable[[float], float], initial_value: Union[int, float], max_iter: int) -> float:
        epsilon = 0.000001
        values: list[float] = [initial_value]
        for i in range(max_iter):
            y = f(values[i])
            values.append(y)
            if abs(values[i] - values[i-1]) < epsilon:
                FixedPoint.values = values
                return y
        print('No solution found, maybe increase max_iter')

class NewtonMethod(Roots): 
    def __str__(self):
        return "Newton Method for roots approximation"
    
    def __call__(self, f: Callable[[float], float], initial_value: int, max_iter: int) -> str:
        self.root = NewtonMethod.newton_method(f, initial_value, max_iter)
        self.iter_table = self.table()
        return f"root converges at {self.root}\nTable:\n{str(self.iter_table)}"
     
    @classmethod 
    def formula(cls, f: Callable[[float], float], x: float) -> float:
        try:
            y = x - f(x)/derivative(f, x)
            return y
        except ZeroDivisionError:
            raise ZeroDivisionError("Could not find root")
    
    @staticmethod
    def newton_method(f: Callable[[float], float], initial_value: int, max_iter: int) -> float:
        epsilon = 0.00001
        values: list[float] = [initial_value]
        for n in range(max_iter):
            y = NewtonMethod.formula(f, values[n])
            values.append(y)
            if abs(values[n] - values[n-1]) < epsilon:
                NewtonMethod.values = values
                return y
        print('No solution found, maybe increase max_iter')
        
class DTDS(Roots):
    def __str__(self):
        return "Discrete-time Dynamical System"


class SDE(Roots):
    ''' interacting species'''
    def __str__(self):
        return "Systems of Difference Equations"
    
    @staticmethod
    def equilibrium(a: float, b: float, c: float, d: float) -> tuple[int, int]:
        return (round((1-c)/d,0), round((a-1)/b,0))
    
    @staticmethod
    def sensitivity_analysis(f: Callable[[float, float], float],
                             g: Callable[[float, float], float],
                             max_iter: int,
                             init_values: tuple[int, int] = (0,0)):
        #storing every output from each function
        values = [[init_values[0]],  #f(x)
                  [init_values[1]]]  #g(x)
        for i in range(max_iter):
            x = f(values[0][i],values[1][i])
            y = g(values[0][i],values[1][i])
            values[0].append(round(x,0))
            values[1].append(round(y,0))
        SDE.values = values
        return values
            
    def table(self) -> dataframe:
        model_iter = pd.DataFrame({
            'F_n': self.values[0],
            'G_n': self.values[1]
            })
        return model_iter
    
    def plot_iterations(self):
        n = len(self.values)
        x = [i for i in range(n)]
        plt.plot(x, self.values[0])
        plt.plot(x, self.values[1])
        plt.xlabel("Iterations")
        plt.ylabel("Root")
        plt.show()
        

    
