import numpy as np
def montecarlo(f, a, b, tol):
    iterations = 0
    max_iter = 100000

    while iterations < max_iter:
        iterations += 1
        x = np.random.uniform(a, b) #Pseudo-random algorithm _> 1 FLOP
        
        if abs(f(x)) < tol:
            return f'Root using Monte Carlo Method: {x}, Number of Iterations: {iterations}, Number of Floating-Point Operations: {iterations}'

f = lambda x: (np.e)**(-x**3)-(x**4)-np.sin(x)

montecarlo(f, 0.5, 0.75, (0.5*(10**-4)))