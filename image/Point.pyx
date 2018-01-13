# distutils: language=c++

cdef extern from "v_repMath/VPoint.h":
    cdef cppclass VPoint:
        VPoint() 
        VPoint(int initX,int initY) 
