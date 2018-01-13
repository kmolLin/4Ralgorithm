from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        Extension(
            "geomConstraintSolver",
            sources=[
                "inverseKinematics/geomConstraintSolver/geometricConstraintSolver.cpp",
                "inverseKinematics/geomConstraintSolver/iKChainCont.cpp",
                "inverseKinematics/geomConstraintSolver/iKChain.cpp",
                "inverseKinematics/geomConstraintSolver/iKDummy.cpp",
                "inverseKinematics/geomConstraintSolver/iKGraphJoint.cpp",
                "inverseKinematics/geomConstraintSolver/iKGraphNode.cpp",
                "inverseKinematics/geomConstraintSolver/iKGraphObjCont.cpp",
                "inverseKinematics/geomConstraintSolver/iKGraphObject.cpp",
                "inverseKinematics/geomConstraintSolver/iKJoint.cpp",
                "inverseKinematics/geomConstraintSolver/iKMesh.cpp",
                "inverseKinematics/geomConstraintSolver/iKObjCont.cpp",
                "inverseKinematics/geomConstraintSolver/iKObject.cpp",
                "v_repMath/3Vector.cpp",
                "v_repMath/3X3Matrix.cpp",
                "v_repMath/4Vector.cpp",
                "v_repMath/4X4FullMatrix.cpp",
                "v_repMath/4X4Matrix.cpp",
                "v_repMath/6Vector.cpp",
                "v_repMath/6X6Matrix.cpp",
                "v_repMath/7Vector.cpp",
                "v_repMath/MMatrix.cpp",
                "v_repMath/MyMath.cpp",
                "v_repMath/Vector.cpp",
                'geomConstraintSolver.pyx',
            ],
            define_macros=[("WIN_VREP", None)]
        ),
        compiler_directives={'boundscheck':True}
    ),
    include_dirs=["inverseKinematics/geomConstraintSolver", "v_repMath"]
)
