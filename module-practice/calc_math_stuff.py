from sympy import diff, sqrt, integrate, Symbol
from math import pi
import wolframalpha as w
import sympy as s
import math as m

# calculate integrals & surface area for function rotated around axis
# https://docs.scipy.org/doc/scipy/tutorial/integrate.html          scipy
# https://docs.sympy.org/latest/modules/functions/index.html        simpy math functions
# https://docs.sympy.org/latest/modules/integrals/integrals.html    simpy integrals
# https://wolframalpha.readthedocs.io/en/latest/?badge=latest       wolframalpha



x = s.Symbol('x')
y = s.Symbol('y')


# INPUTS ------
a = 0                   #interval
b = 6


F = (1/3) * (x**2 + 2)**(3/2)                #function




# DERIVITIVE ---------------

def derivative():
    dx = diff(F)
    print("derivative:    ")
    print(dx)
    return dx






# DEFINITE INTEGRAL ----------------

def integral():
    Id = integrate(F, (x, a, b))
    Ii = integrate(F, x)
    print("\nindefinite integral:\n")
    print(Ii)
    print("\ndefinite integral:\n")
    print(Id)
    return Id






# EXACT LENGTH ---------------

def arc_length():
    dx = diff(F)
    z = sqrt(1 + (dx)**2)
    I = integrate(z, (x, a, b))
    print("arc length:    \n")
    print(I)
    return I





# SURFACE AREA ---------------

def surface_area():
    dx = diff(F) 
    v = sqrt(1 + (dx)**2)
    z = v * F * 2 * pi
    I = integrate(z, (x, a, b))
    print("surface area:    ")
    print(I)
    return I





if __name__ == "__main__":
    #surface_area()
    #arc_length()
    integral()
    #derivative()


