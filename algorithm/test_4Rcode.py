from math import (
radians, degrees, 
sin, cos, atan2# (y,x)
, asin, sqrt
)
from time import time
from sympy import *

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# setting four degree
a1 = 60
a2 = 40
a3 = 60
a4 = 50
a5 = 50
a6 = 40

theta2 = 52.79  #interable in 0~2*pi
theta4 = 82.92

radians(10)
r = 80

corrdinateA = (r*1, 0, 0)
corrdinateB = (r*cos(radians(a1)), r*sin(radians(a1)), 0)  # correct
corrdinateC = (
    r*(cos(radians(a1))*cos(radians(a2))-(sin(radians(a1))*sin(radians(a2))*cos(radians(theta2)))), 
    r*(sin(radians(a1))*cos(radians(a2))+cos(radians(a1))*sin(radians(a2))*cos(radians(theta2))),
    r*(sin(radians(a2))*sin(radians(theta2)))
)
corrdinateD = (r*(cos(radians(a4))), r*(sin(radians(a4))*cos(radians(theta4))), r*sin(radians(a4))*sin(radians(theta4)))

def callD(corrdinate):
    return(corrdinate[0], corrdinate[1], corrdinate[2])


def inversdistance(r, theta5):
    return sqrt(r**2+r**2-2*(cos(radians(theta5)))*r**2)

def distance(a, b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)

def releative(theta2, r):
    #C dot D = cos(a3)  correct
    A = sin(radians(a1))*cos(radians(a2))*sin(radians(a4))+cos(radians(a1))*sin(radians(a2))*sin(radians(a4))*cos(radians(theta2))
    B = sin(radians(a2))*sin(radians(a4))*sin(radians(theta2))
    C = cos(radians(a1))*cos(radians(a2))*cos(radians(a4))-cos(radians(a3))-sin(radians(a1))*sin(radians(a2))*cos(radians(a4))*cos(radians(theta2))

    anser = 2*atan2((-B-sqrt(A**2+B**2-C**2)), (C-A))
    return degrees(anser)%360

def coodernate(a1, a2, a3, a4, a5, a6, r, theta2, theta4):
    Apoint = (r*1, 0, 0)
    Bpoint = (r*cos(radians(a1)), r*sin(radians(a1)), 0)  # correct
    Cpoint = (
        r*(cos(radians(a1))*cos(radians(a2))-(sin(radians(a1))*sin(radians(a2))*cos(radians(theta2)))), 
        r*(sin(radians(a1))*cos(radians(a2))+cos(radians(a1))*sin(radians(a2))*cos(radians(theta2))),
        r*(sin(radians(a2))*sin(radians(theta2)))
    )
    Dpoint = (r*(cos(radians(a4))), r*(sin(radians(a4))*cos(radians(theta4))), r*sin(radians(a4))*sin(radians(theta4)))
    return Cpoint, Dpoint
    
def getEpoint(cx,cy, cz, dx, dy, dz, r, a5, a6):
    
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    f1 = (x-dx)**2+(y-dy)**2+(z-dz)**2-inversdistance(r, a5)**2
    f2 = x**2+y**2+z**2-r**2
    f3 = (x-cx)**2+(y-cy)**2+(z-cz)**2-inversdistance(r, a6)**2
    sol = solve((f1, f2, f3), x, y, z)
    return sol
    


if __name__=='__main__':
    t0 = time()
    x1 = []
    y1 = []
    z1 = []
    x2 = []
    y2 = []
    z2 = []
    E1 = []
    Ex1 = []
    Ey1 = []
    Ez1 = []
    E2 = []
    Ex2 = []
    Ey2 = []
    Ez2 = []
    #l = [f"{t}\t{releative(t, r)}" for t in range(0, 360)]
    #print("\n".join(l))
    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    for i in range(0, 360):
        l = releative(i, r)
        a = (coodernate(a1, a2, a3, a4, a5, a6, r , i, l ))
        # Cpoint
        
        cx, cy, cz = callD(a[0])
        dx, dy, dz = callD(a[1])
        
        #print(cx,"\t", cy,"\t", cz,"\t")
        x1.append(cx)
        y1.append(cy)
        z1.append(cz)
        
        x2.append(dx)
        y2.append(dy)
        z2.append(dz)
        #print(x1[i], y1[i], z1[i], x2[i], y2[i], z2[i], r, a5, a6)
        Epoint = getEpoint(x1[i], y1[i], z1[i], x2[i], y2[i], z2[i], r, a5, a6)
        E1.append(Epoint[0])
        E2.append(Epoint[1])
        
        ex, ey, ez = callD(E1[i])
        ex1, ey1, ez1 = callD(E2[i])
        #print(ex,"\t", ey,"\t", ez,"\t")
        
        Ex1.append(ex)
        Ey1.append(ey)
        Ez1.append(ez)
        
        Ex2.append(ex1)
        Ey2.append(ey1)
        Ez2.append(ez1)
    print(E1)
    
        
    #print(Ex1)
    ax.plot(x1, y1, z1, label='C point')
    ax.plot(x2, y2, z2, label='D point')
    ax.plot(Ex1, Ey1, Ez1, label='E1 point')
    ax.plot(Ex2, Ey2, Ez2, label='E2 point')
    ax.legend()
    plt.show()
    
    
    #print(distance(corrdinateC, corrdinateD))
    #print(inversdistance(r, a5))
    #print(inversdistance(r, a6))
    
    


    """
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
    """
    corrdinateA = (r*1, 0, 0)
    corrdinateB = (r*cos(radians(a1)), r*sin(radians(a1)), 0)  # correct
    corrdinateC = (
        r*(cos(radians(a1))*cos(radians(a2))-(sin(radians(a1))*sin(radians(a2))*cos(radians(theta2)))), 
        r*(sin(radians(a1))*cos(radians(a2))+cos(radians(a1))*sin(radians(a2))*cos(radians(theta2))),
        r*(sin(radians(a2))*sin(radians(theta2)))
    )
    corrdinateD = (r*(cos(radians(a4))), r*(sin(radians(a4))*cos(radians(theta4))), r*sin(radians(a4))*sin(radians(theta4)))
    """
    
    # get E point need C point , D point ,Radin in circle a5 a6 to get inverdistance in tricangle
    #cx, cy, cz = callD(corrdinateC)
    #dx, dy, dz = callD(corrdinateD)
    #f1 = (x-dx)**2+(y-dy)**2+(z-dz)**2-inversdistance(r, a5)**2
    #f2 = x**2+y**2+z**2-r**2
    #f3 = (x-cx)**2+(y-cy)**2+(z-cz)**2-inversdistance(r, a6)**2
    
    #sol = solve((f1, f2, f3), x, y, z)
    


    #print(sol)
    #print(distance(sol[0], corrdinateD), distance(sol[0], corrdinateC))
    #print(distance(sol[1], corrdinateD), distance(sol[1], corrdinateC))
    
