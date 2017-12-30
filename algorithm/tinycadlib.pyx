from libc.math cimport (
sin, cos, atan2, asin, sqrt
)
import numpy as np
cimport numpy as np
# np.deg2rad  or np.rad2deg

nan = float("nan")

cdef class Coordinate(object):
    cdef public double x
    cdef public double y
    cdef public double z
    
    def __cinit__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    cpdef public double distance(self, Coordinate obj):
        return sqrt(pow(self.x-obj.x, 2) + pow(self.y-obj.y, 2) + pow(self.z-obj.z, 2))

cpdef object threePoints(Coordinate A, double L0, double a0, Coordinate B, bool reverse=False):
    cdef double b0 = atan2((B.y - A.y), (B.x - A.x))
    if reverse:
        return (A.x + L0*sin(b0 - a0), A.y + L0*cos(b0 - a0))
    else:
        return (A.x + L0*sin(b0 + a0), A.y + L0*cos(b0 + a0))
        

cpdef object releative(double theta2, double a1, double a2, double a3, double a4):
    #C dot D = cos(a3)  correct
    
    cdef double A = sin(np.deg2rad(a1))*cos(np.deg2rad(a2))*sin(np.deg2rad(a4))+cos(np.deg2rad(a1))*sin(np.deg2rad(a2))*sin(np.deg2rad(a4))*cos(np.deg2rad(theta2))
    cdef double B = sin(np.deg2rad(a2))*sin(np.deg2rad(a4))*sin(np.deg2rad(theta2))
    cdef double C = cos(np.deg2rad(a1))*cos(np.deg2rad(a2))*cos(np.deg2rad(a4))-cos(np.deg2rad(a3))-sin(np.deg2rad(a1))*sin(np.deg2rad(a2))*cos(np.deg2rad(a4))*cos(np.deg2rad(theta2))

    # TODO
    return 2*atan2((-B-sqrt(A**2+B**2-C**2)), (C-A))
    
