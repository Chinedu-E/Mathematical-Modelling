import sympy as sym
class CublicSpline:
    def __init__(self,x,y):
        S1 = 0
        S2 = 0
        if len(x) != 3 or len(y) != 3:
            print('Please enter a cubic spline model i.e data of 3 points')
        else:
            self.x = x
            self.y = y
            
    def __str__(self):
        return ""
            
    def poly_coefficients(self):
        x = self.x
        y = self.y
        a1, b1, c1, d1 = sym.symbols('a1 b1 c1 d1')
        a2, b2, c2, d2 = sym.symbols('a2 b2 c2 d2')
        #conditions
        eq1 = sym.Eq(a1 + x[0]*b1+ x[0]*c1**2+ x[0]*d1**3, y[0])
        eq2 = sym.Eq(a1 + x[1]*b1+ x[1]*c1**2+ x[1]*d1**3, y[1])
        eq3 = sym.Eq(a2 + x[1]*b2+ x[1]*c2**2+ x[1]*d2**3, y[1])
        eq4 = sym.Eq(a2 + x[2]*b2+ x[2]*c2**2+ x[2]*d2**3, y[2])
        eq5 = sym.Eq(b1+ c1*2*x[1] + 3*d1*x[1]**2, b2+ c2*2*x[1] + 3*d2*x[1]**2)
        eq6 = sym.Eq(2*c1 +6*d1*x[1], 2*c2 +6*d2*x[1])
        eq7 = sym.Eq(2*c1 + 6*d1*x[0], 0)
        eq8 = sym.Eq(2*c2 + 6*d2*x[2], 0)
        conditions = {eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8}
        t = sym.solve(conditions, cubics=False)
        print(t[0].keys())
        t = sym.simplify(t[0][b1])
        print(t)
    
    
CublicSpline([1,2,3],[5,8,25]).poly_coefficients()