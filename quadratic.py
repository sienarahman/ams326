import numpy as np
import math
def quadratic(t, y, tvalue): 
    n = len(t)
    
    A = np.column_stack((np.ones(n), t, t**2)) # n multiplications, n = 5 -> 5 FLOPs

    # A^T * A
    A_TxA = np.dot(A.T, A) # Multiplying two 3x3 matrices -> 18 multiplications times n
    
    # A^T * y
    A_Txy = np.dot(A.T, y) # Multiplying a 3x3 matrix and a 3-vector -> 6 multiplications times n

    # A^T * x = A^T*y -> solve for x
    coeffs = np.linalg.solve(A_TxA, A_Txy) # Two 3x3 Matrices, Gaussian Elimination Procedure, 3^3 -> 27 FLOPs

    a0, a1, a2 = coeffs

    # Interpolated Q_2 equation
    print(f"Q_2(t) = {a0} + {a1}t + {a2}t^2")   
    
    # Q_2 at t = 6
    t6 = a0 + (a1 * tvalue) + (a2 * tvalue**2) # Addition, Multiplication, Addition, Multiplication, Exponeniation -> 5 FLOPs
    
    flops = n + (18*n) + (6*n) + 27 + 5

    return (f'The interpolated stock closing value on session 6 (t = 6): {t6:0.1f}, Number of Iterations: 1, Number of Floating-Point Operations: {flops}')

t = np.array([5, 4, 3, 2, 1])
y = np.array([417, 398, 397, 407, 412])

quadratic(t, y, 6)
