# Euler method to solve differential equations
import diff_eqs

def euler_OEK(t0, ti, x0, xi, num, k1, k2):
    h = ti -t0
    
    # Call differential equations 
    for i in range(0, num):
        xi[i] = x0[i] + h * diff_eqs.diff_eqs(x0, num, k1, k2)[i]

    return ti, x0, xi
