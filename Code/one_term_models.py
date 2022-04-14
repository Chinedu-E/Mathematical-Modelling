import matplotlib.pyplot as plt
import numpy as np

class OneTerm:
    def __init__(self,x, y):
        self.x = x
        y = np.array(y)
        self.y = y
        self.ladder = [1/(y**2),1/y,1/np.sqrt(y),np.log(y),np.sqrt(y),
                       y,
                       y**2,y**3,y**4,y**5]
        self.slider = 5
    
    def plot(self, xlab: str = 'x', ylab: str = 'y'):
        plt.plot(self.x,self.ladder[self.slider])
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.show()
    
    def go_up(self):
        self.slider += 1
    
    def go_down(self):
        self.slider -= 1
    
