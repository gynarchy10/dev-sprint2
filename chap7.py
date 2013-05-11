# Enter your answers for chapter 7 here
# Name: Jenna Gopilan

from math import *
# Ex. 7.5

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def estimate_pi():
    """
    Based on the formula - calculate an estimate of pi
    """
    constant = ((2*(sqrt(2))/9801))
    summationfinal = 0
    k = 0
    while True:
        is_top = ((factorial(4*k))*(1103 + 26390*k))
        is_bottom = ((factorial(k)**4)*396**(4*k))
        term = (1.0 * is_top)/is_bottom
        summationfinal += term
        if term < 1e-15:
#            print k
            break 
        k += 1
    return 1.0/(summationfinal * constant)
    
a = estimate_pi()
print a 


# How many iterations does it take to converge?

# It took 4 iterations for it converge.