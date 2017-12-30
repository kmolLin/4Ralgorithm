from libc.math cimport isnan
import tinycadlib
from tinycadlib import (
    Coordinate, 
    releative
)
import numpy as np
cimport numpy as np

cdef class build_plan(object):
    
    def __cinit__(self, object mechanismParams):
        self.VARS = mechanismParams['VARS']
        #target point
        self.targetPoint = mechanismParams['Target']
        # counting how many action to satisfied require point
        self.POINTS = len(mechanismParams['targetPath'])
        # driving point, string
        self.Driving = mechanismParams['Driving']
        # folower point, string
        self.Follower = mechanismParams['Follower']
        #constraint
        self.constraint = mechanismParams['constraint']
        
        cdef int i
        # use tuple data, create a list of coordinate object
        #[Coordinate(x0, y0), Coordinate(x1, y1), Coordinate(x2, y2), ...]
        self.target = np.ndarray((self.POINTS,), dtype=np.object)
        
        for i, (x, y, z) in enumerate(mechanismParams['targetPath']):
            self.target[i] = Coordinate(x, y, z)
            
        self.Expression_str = mechanismParams['Expression']
        ExpressionL = mechanismParams['Expression'].split(';')
        
        # Link L0, L1, L2, L3, ...
        self.Link = []
        
        cdef str expr, p
        
        
    cpdef object get_path(self):
        return [(c.x, c.y) for c in self.target]
    
    cpdef str get_Driving(self):
        return self.Driving
    
    cpdef str get_Follower(self):
        return self.Follower
    
    cpdef str get_Target(self):
        return self.targetPoint
    
    cpdef object get_Link(self):
        return self.Link
    
    cpdef str get_Expression(self):
        return self.Expression_str
