import numpy as np
def secant(f, df, x_imin1, x_i, tol):
    iterations = 0
    max_iter = 1000
    
    while iterations < max_iter:
        iterations += 1
        if abs(f(x_i)) < tol:
            return (f'Root using Secant Method: {x_i}, Number of Iterations: {iterations}, Number of Floating-Point Operations: {iterations * 6}')
        else:
            # Secant equation for x_iplus1
            x_iplus1 = x_i - (f(x_i) / ((f(x_i) - f(x_imin1)) / (x_i - x_imin1))) # <- Subtraction, Division, Subtraction, Division, Subtraction <- 5 FLOPs
            x_imin1 = x_i
            x_i = x_iplus1

f = lambda x: (np.e)**(-x**3)-(x**4)-np.sin(x)
df = lambda x: (-4*(x**3))-(3*(x**2)*(np.e)**(-x**3))-np.cos(x)

secant(f, df, -1, 1, (0.5*(10**-4)))