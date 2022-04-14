from numpy import array, around
import unittest
from Code.matrix_computations import MatrixMethods as matrix

class TestMatrixComputations(unittest.TestCase):
    
    def test_eigen_estimates(self):
        A = array([[5, -2, 2],
                   [2, 0, 4],
                   [4, 2, 7]])
        result = matrix.eigen_estimates(A)
        exp = [(1, 9),
               (-6, 6),
               (1, 13)]
        self.assertEqual(result, exp)
        
        
    def test_gauss_seidel(self):
        A = array([[16, 3],
                   [7, -11]])
        b = array([11, 13])
        x0 = array([1,1])
        result = matrix(A, b).gauss_seidel(x0, 8)
        exp = [0.8122, -0.665]
        self.assertEqual(list(around(result,4)), exp)
    
    
    def test_cholesky_decomposition1(self):
        A = array([[4, 2, 14],
                   [2, 17, -5],
                   [14, -5, 83]])
        b = array([14, -101, 155])
        result = matrix(A, b).cholesky_decomposition()
        exp = [3, -6, 1]
        self.assertEqual(list(around(result, 0)), exp)
    
    
    def test_cholesky_decomposition2(self):
        A = array([[9, 12, 6],
                   [12, 25, 11],
                   [6, 11, 14]])
        b = array([6.9, 10.7, 6.9])
        result = matrix(A, b).cholesky_decomposition()
        exp = [0.5, 0.1, 0.2]
        self.assertEqual(list(around(result, 1)), exp)
    
    def test_LU_decompose(self):
        A = array([[1, 2, 4],
                   [3, 8, 14],
                   [2, 6, 13]])
        b = array([3, 13, 4])
        result = matrix(A, b).LU_decompose()
        exp = [3, 4, -2]
        self.assertEqual(list(around(result, 0)), exp)
    
    def test_true_solution(self):
        A = array([[16, 3],
                   [7, -11]])
        b = array([11, 13])
        result = matrix(A, b).true_solution()
        exp = [0.8122, -0.665]
        self.assertEqual(list(around(result,4)), exp)
        
        
        
        
if __name__ == '__main__':
    unittest.main()