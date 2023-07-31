# Define the differential equations
import numpy as np
def diff_eqs(x, n, k1, k2):
    
    dx = np.zeros(n)

    # Define differential equations here: 
    dx[0] = -k1 * x[0]
    dx[1] = k1 * x[0] - k2 * x[1]
    dx[2] = k2 * x[1]
    
    return dx    



