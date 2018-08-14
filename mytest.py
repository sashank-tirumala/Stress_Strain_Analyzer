from sympy import *

x = Symbol('x')

c = []
c.append(3)
c.append(2)
expr = c[0]*(x**c[1])
print(expr)
print(integrate(expr,x))
