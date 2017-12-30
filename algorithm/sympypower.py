from time import time
from sympy import *
#x, y, z = symbols('x y z')
x, y, z, dx, dy, dz, cx, cy, cz, ed, ec, r = symbols('x y z dx dy dz cx cy cz ed ec r')
"""
y = Symbol('y')
z = Symbol('z')
dx = Symbol('dx')
dy = Symbol('dy')
dz = Symbol('dz')
cx = Symbol('cx')
cy = Symbol('cy')
cz = Symbol('cz')
ed = Symbol('ed')
ec = Symbol('ec')
r = Symbol('r')
"""
#f1 = (-2*dx+2*cx)*x+((-2*dy+2*cy)*y)+((-2*dz+2*cz)*z)-(inversdistance(r, a5)**2+inversdistance(r, a6)**2)
#f2 = (-2*cx)*x+(-2*cy)*y+(-2*cz)*z-inversdistance(r, a6)**2+2*r**2
#f3 = (-2*dx)*x+(-2*dy)*y+(-2*dz)*z-inversdistance(r, a6)**2+2*r**2  
#f4 = x**2+y**2+z**2-r**2


t0 = time()
f1 = (x-dx)**2+(y-dy)**2+(z-dz)**2-ed**2
f2 = x**2+y**2+z**2-r**2
f3 = (x-cx)**2+(y-cy)**2+(z-cz)**2-ec**2

sol = solve([f1, f2, f3], [x, y, z])
print(time()-t0)
#print(sol)
for i in len(sol):
    print(sol[i])


