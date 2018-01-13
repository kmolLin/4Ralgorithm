# distutils: language=c++

cdef extern from "v_repMath/4x4Matrix.h":        
    cdef cppclass C4X4Matrix

cdef extern from "v_repMath/3Vector.h":
    cdef cppclass C3Vector:
        C3Vector()
        C3Vector(float v0,float v1,float v2)
        C3Vector(float v[3])
        C3Vector(C3Vector& v)
        float* ptr()

cdef extern from "v_repMath/4Vector.h":
    cdef cppclass C4Vector:  
        C4Vector()
        C4Vector(float v0,float v1,float v2,float v3)
        C4Vector(float v[4])
        C4Vector(C3Vector& v)
        C4Vector(C4Vector& q)
        C4Vector(float a,float b,float g)
        C4Vector(float angle, C3Vector& axis)
        C4Vector(C3Vector& startV, C3Vector& endV)


        C3Vector getEulerAngles()
        
cdef extern from "v_repMath/6Vector.h":
    cdef cppclass C6Vector:
        C6Vector()
        C6Vector(float v0,float v1,float v2,float v3,float v4,float v5)
        C6Vector( float v[6])
        C6Vector(C3Vector& v0, C3Vector& v1)
        C6Vector(C6Vector& v)


        void clear()
        
cdef extern from "v_repMath/7Vector.h":
    cdef cppclass C7Vector:
        C7Vector()
        C7Vector(C7Vector& v)
        C7Vector(C4Vector& q)
        C7Vector(C3Vector& x)
        C7Vector(C4Vector& q,const C3Vector& x)
        C7Vector(float m[4][4])
        C7Vector(C4X4Matrix& m)
        C7Vector(float angle,const C3Vector& pos,const C3Vector& dir)

        
cdef extern from "v_repMath/Vector.h":
    cdef cppclass CVector:
        CVector()
        CVector(int nElements)
        CVector(C3Vector& v)
        CVector(C4Vector& v)
        CVector(C6Vector& v)
        CVector(C7Vector& v)
        CVector(CVector& v)

        
