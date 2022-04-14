import os
import datetime
import numpy as np
import pandas as pd
import sympy as sym
import scipy
from scipy.misc import derivative
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

class StraightFit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a, self.b = np.polyfit(x,y,1)
        self.r2 = r2_score()
    def plot(self):
        pass
    
class PowerFit:
    pass


class Fit2(PowerFit):
    pass

class ExpFit:
    def __init__(self):
        pass
    
