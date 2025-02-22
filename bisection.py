import numpy as np
def bisection(f, a, b, tol): 
   #1. Select initial value, a and b, to bracket the root in [a, b] with condition:
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) * f(b) must be < 0.")

    iterations = 0
    while (b - a) / 2 > tol:
        #2. Compute the mid-point of the values a and b.
        x = (a + b) / 2 # Addition, Division -> 2 Floating-Point Operations (FLOPs)
        
        if f(x) == 0:
            return (f"Root using Bisection Method: {x}, Number of Iterations: {iterations}, Number of Floating-Point Operations: {iterations * 3}")

        #3. Assess which half contains the root by
        elif f(a) * f(x) < 0: # Multiplication -> 1 FLOP
            #If f(a) * f(c) < 0 then the root must be in [a, c] and you narrow the bracket by setting:
            b = x
        else:
            #Otherwise, the root is in [x, b] and you narrow the bracket by setting:
            a = x

        iterations += 1

    return (f"Root using Bisection Method: {x}, Number of Iterations: {iterations}, Number of Floating-Point Operations: {iterations * 3}")

f = lambda x: (np.e)**(-x**3)-(x**4)-np.sin(x)

bisection(f, -1, 1, (0.5*(10**-4)))