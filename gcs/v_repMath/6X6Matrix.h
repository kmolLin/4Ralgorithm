// This file is part of V-REP, the Virtual Robot Experimentation Platform.
// 
// Copyright 2006-2017 Coppelia Robotics GmbH. All rights reserved. 
// marc@coppeliarobotics.com
// www.coppeliarobotics.com
// 
// V-REP is dual-licensed, under the terms of EITHER (at your option):
//   1. V-REP commercial license (contact us for details)
//   2. GNU GPL (see below)
// 
// GNU GPL license:
// -------------------------------------------------------------------
// V-REP is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// V-REP IS DISTRIBUTED "AS IS", WITHOUT ANY EXPRESS OR IMPLIED
// WARRANTY. THE USER WILL USE IT AT HIS/HER OWN RISK. THE ORIGINAL
// AUTHORS AND COPPELIA ROBOTICS GMBH WILL NOT BE LIABLE FOR DATA LOSS,
// DAMAGES, LOSS OF PROFITS OR ANY OTHER KIND OF LOSS WHILE USING OR
// MISUSING THIS SOFTWARE.
// 
// See the GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with V-REP.  If not, see <http://www.gnu.org/licenses/>.
// -------------------------------------------------------------------
//
// This file was automatically created for V-REP release V3.4.0 rev. 1 on April 5th 2017

#pragma once

#include "mathDefines.h"
#include "6Vector.h"
#include "3X3Matrix.h"

class C6X6Matrix  
{
public:
    C6X6Matrix();
    C6X6Matrix(const C6X6Matrix& m);
    C6X6Matrix(const C3X3Matrix& m00,const C3X3Matrix& m01,const C3X3Matrix& m10,const C3X3Matrix& m11);
    ~C6X6Matrix();

    void clear();
    void setMultResult(const C6X6Matrix& m1,const C6X6Matrix& m2);
    void setIdentity();

    C6X6Matrix operator* (const C6X6Matrix& m) const;
    C6X6Matrix operator+ (const C6X6Matrix& m) const;
    C6X6Matrix operator- (const C6X6Matrix& m) const;

    void operator*= (const C6X6Matrix& m);
    void operator+= (const C6X6Matrix& m);
    void operator-= (const C6X6Matrix& m);

    C6Vector operator* (const C6Vector& v) const;
    C6X6Matrix& operator= (const C6X6Matrix& m);

    inline void getInternalData(float d[36]) const
    {
        M[0][0].getInternalData(d+0);
        M[0][1].getInternalData(d+9);
        M[1][0].getInternalData(d+18);
        M[1][1].getInternalData(d+27);
    }
    inline void setInternalData(const float d[36])
    {
        M[0][0].setInternalData(d+0);
        M[0][1].setInternalData(d+9);
        M[1][0].setInternalData(d+18);
        M[1][1].setInternalData(d+27);
    }
    inline float& operator() (unsigned i,unsigned j)
    {
        return(M[i/3][j/3](i%3,j%3));
    }
    inline const float& operator() (unsigned i,unsigned j) const
    {
        return(M[i/3][j/3](i%3,j%3));
    }

    C3X3Matrix M[2][2];
};

