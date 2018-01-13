# distutils: language=c++

from libcpp cimport bool
from libcpp.vector cimport vector
cimport MyMath
from MyMath cimport (
        C7Vector, 
        C4Vector, 
)



cdef extern from "inverseKinematics/geomConstraintSolver/iKGraphNode.h":
    cdef cppclass CIKGraphNode:
        CIKGraphNode()

cdef extern from "inverseKinematics/geomConstraintSolver/iKGraphObject.h":    
    cdef cppclass CIKGraphObject:
        CIKGraphObject()
        CIKGraphObject(C7Vector& cumulTransf,C7Vector& targetCumulTransf) # Tip object
        CIKGraphObject(C7Vector& cumulTransf)

cdef extern from "inverseKinematics/geomConstraintSolver/iKGraphJoint.h":
    cdef cppclass CIKGraphJoint:
        CIKGraphJoint(bool isRevolute,float theParameter,float theMinVal,float theRange,float theScrewPitch,bool isCyclic,float theWeight)
        CIKGraphJoint(C4Vector& theSphericalTr,float theRange,float theWeight)



cdef extern from "inverseKinematics/geomConstraintSolver/iKGraphObjCont.h":        
    cdef cppclass CIKGraphObjCont:
        CIKGraphObjCont()
        CIKGraphNode* getNodeFromUserData0(int userData)
        CIKGraphNode* getNodeFromUserData1(int userData)
        CIKGraphNode* getNodeFromNodeID(int nodeID)
        CIKGraphObject* insertPassiveObjectNode(C7Vector& transformation) # C7???
        CIKGraphObject* insertTipObjectNode(const C7Vector& transformation,const C7Vector& targetTransformation)
        CIKGraphJoint* insertRevoluteJointNode(C7Vector& transformation,float parameter,float minVal,float range,float screwPitch,bool isCyclic,float weight)
        CIKGraphJoint* insertPrismaticJointNode(C7Vector& transformation,float parameter,float minVal,float range,float weight)
        CIKGraphJoint* insertBallJointNode(C7Vector& transformation,C4Vector sphericalTransformation,float range,float weight)
        void resetExplorationIDs()
        int identifyElements()
        void putElementsInPlace()
        void replaceElementIDWithAnother(int oldID,int newID)
        
        void getLinkObjectsWithElementID(int elementID,vector[CIKGraphObject*]& links)
        void preMultiplyObjectsWithElementID(int elementID,C7Vector& transform)
        void actualizeAllTransformations()
        void setBaseObject(int nodeID)
        
        CIKGraphObject* getBaseObject()
        int baseObjectID
        int nodeIDCounter
        int numberOfElementIDs
        void emptyContainer()
        
        
cdef extern from "inverseKinematics/geomConstraintSolver/geometricConstraintSolver.h":   
    cdef struct SGeomConstrSolverParam:
        int maxIterations
        float interpolation
        float generalDamping
        float maxAngularVariation
        float maxLinearVariation
        float loopClosurePositionTolerance
        float loopClosureOrientationTolerance

    cdef cppclass CGeometricConstraintSolver:
        @staticmethod
        bool solve(CIKGraphObjCont& graphContainer,SGeomConstrSolverParam& parameters)
    
