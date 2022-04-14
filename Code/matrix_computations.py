import numpy as np


class MatrixMethods:

    @classmethod
    def _shape_checker(cls,A: np.ndarray, b: np.ndarray) -> None:
        try:
            if A.shape[0] != A.shape[1]:
                raise ValueError("A must be a square matrix")
        except IndexError:
            raise ValueError("A must be a 2D matrix")
        try:
            _ = b.shape[1]
            raise ValueError("b must be a column vector")
        except IndexError:
            pass
        return
    
    
    def lu(self) -> tuple[np.ndarray, np.ndarray]:
        '''Gotten from https://johnfoster.pge.utexas.edu/numerical-methods-book/LinearAlgebra_LU.html'''
        #Get the number of rows
        n = self.A.shape[0]

        U = np.zeros((n, n), dtype=np.double)
        L = np.eye(n, dtype=np.double)

        #Loop over rows
        for k in range(n):
            U[k, k:] = self.A[k, k:] - L[k,:k] @ U[:k,k:]
            L[(k+1):,k] = (self.A[(k+1):,k] - L[(k+1):,:] @ U[:,k]) / U[k, k]
    
        return L, U
    
        
    def __init__(self,A: np.ndarray, b: np.ndarray):
        self._shape_checker(A, b)
        self.A = A
        self.b = b
        self.L = np.tril(A) # upper triangular matrix
        self.U = np.triu(A, 1) # lower triangular matrix
        
        
    def __str__(self):
        return self.__class__.__name__
    
    
    def LU_decompose(self) -> np.ndarray:
        L, U = self.lu()
        l_inv = np.linalg.inv(L)
        u_inv = np.linalg.inv(U)
        #Solve Ly = b.
        y = np.dot(l_inv, self.b)
        #Solve Ux = y.
        x = np.dot(u_inv, y)
        return x

    
    def cholesky_decomposition(self) -> np.ndarray:
        ''' Solving A = GG^T'''
        G =  np.linalg.cholesky(self.A)
        g_inv = np.linalg.inv(G)
        g_trans = np.transpose(G)
        g_trans_inv = np.linalg.inv(g_trans)
        #Solve Gy = b.
        y = np.dot(g_inv, self.b)
        #Solve G^Tx = y.
        x = np.dot(g_trans_inv, y)
        return x
    
         
    def gauss_seidel(self, initial_guess: np.ndarray, n: int) -> np.ndarray:
        x = [initial_guess]
        l_inv = np.linalg.inv(self.L)
        for i in range(n):
            solution = np.dot(l_inv,(self.b - np.dot(self.U ,x[i])))
            x.append(solution)
        return x[-1]
    
    
    def true_solution(self) -> np.ndarray:
        return np.dot(np.linalg.inv(self.A), self.b)
    
    
    @staticmethod
    def eigen_estimates(A: np.ndarray) -> list[tuple]:
        MatrixMethods._shape_checker(A, b= np.array([0]))
        out = []
        n = A.shape[0]
        for i in range(n):
            row_sum = 0
            for j in range(n):
                if i==j:
                    lhs = A[i][i]
                else:
                    row_sum += abs(A[i][j])
            upper_bound = row_sum + lhs
            lower_bound = lhs - row_sum
            out.append((lower_bound, upper_bound))
        return out