# distutils: language=c++

cdef extern from "v_repMath/3Vector.h":
    cdef cppclass C3Vector

cdef extern from "v_repMath/4Vector.h":
    cdef cppclass C4Vector

cdef extern from "v_repMath/7Vector.h":
    cdef cppclass C7Vector

cdef extern from "v_repMath/3x3Matrix.h":
    cdef cppclass C3X3Matrix:
        C3X3Matrix()
        C3X3Matrix(C4Vector& q)
        C3X3Matrix(C3X3Matrix& m)
        C3X3Matrix(C3Vector& xAxis, C3Vector& yAxis, C3Vector& zAxis)

cdef extern from "v_repMath/4x4Matrix.h":        
    cdef cppclass C4X4Matrix:
        C4X4Matrix()
        C4X4Matrix(C4X4Matrix& m)
        C4X4Matrix(CMatrix& m)
        C4X4Matrix(float m[4][4])
        C4X4Matrix(C3X3Matrix& m, C3Vector& x)
        C4X4Matrix(C3Vector& x, C3Vector& y, C3Vector& z, C3Vector& pos)
        C4X4Matrix(C7Vector& transf)

cdef extern from "v_repMath/4X4FullMatrix.h":
    cdef cppclass C4X4FullMatrix:
        C4X4FullMatrix()   # Needed for serialization
        C4X4FullMatrix(C4X4Matrix& m)
        C4X4FullMatrix(C4X4FullMatrix& m)

        
cdef extern from "v_repMath/6X6Matrix.h":
    cdef cppclass C6X6Matrix:
        C6X6Matrix()
        C6X6Matrix(C6X6Matrix& m)
        C6X6Matrix(C3X3Matrix& m00,C3X3Matrix& m01, C3X3Matrix& m10, C3X3Matrix& m11)

        
cdef extern from "v_repMath/MMatrix.h":
    cdef cppclass CMatrix:
        CMatrix()
        CMatrix(int nRows,int nCols)
        CMatrix(C3X3Matrix& m)
        CMatrix(C4X4Matrix& m)
        CMatrix(C6X6Matrix& m)
        CMatrix(CMatrix& m)

        
