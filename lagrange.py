import numpy as np
def lagrange(t, y, tvalue):
    P_4 = 0
    iterations = 0
    for i in range(5):
        n = len(t)
        iterations += 1
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (tvalue - t[j]) / (t[i] - t[j]) # Multiplication, Subtraction, Division, Subtraction <- 4 FLOPs
        
        P_4 += y[i] * L_i # Addition, Multiplication <- 2 FLOPs

    return (f'The interpolated stock closing value on session 6 (t = 6): {P_4}, Number of Iterations: {iterations}, Number of Floating-Point Operations: {iterations * 6}')

t = np.array([5, 4, 3, 2, 1])
y = np.array([417, 398, 397, 407, 412])

lagrange(t, y, 6)