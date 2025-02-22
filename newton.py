import numpy as np
np.set_printoptions(legacy='1.25')
def newton(f, df, x0, tol):
    iterations = 0
    max_iter = 1000
    
    while iterations < max_iter:
        iterations += 1
        if abs(f(x0)) < tol:
            return (f'Root using Newton Method: {x0}, Number of Iterations: {iterations}, Number of Floating-Point Operations: {iterations * 2}')
        else:
            # Newton equation for x_iplus1
            x0 = x0 - (f(x0) / df(x0)) # Subtraction, Division -> 2 FLOPs

f = lambda x: (np.e)**(-x**3)-(x**4)-np.sin(x)
df = lambda x: (-4*(x**3))-(3*(x**2)*(np.e)**(-x**3))-np.cos(x)

newton(f, df, 0, (0.5*(10**-4)))