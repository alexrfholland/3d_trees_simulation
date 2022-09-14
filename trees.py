from unicodedata import name
import pandas as pd
import settings as set
from typing import List
from typing import Dict
import math
import numpy as np

import rhino3dm

path = set.IMPORTFOLDER2 + 'clampedData.csv'
data = pd.read_csv(path)
data.set_index('Tree', inplace = True)
data.columns = [c.replace(' ', '_') for c in data.columns]



"""trees: List[pd.DataFrame] = []
for i in range(1,17):
    tree = data.query(f'Tree == {i}')
    trees.append[tree]
"""


def MakePt(x):
    pt: rhino3dm.Point3d = rhino3dm.Point3d(x.posX, x.posY, x.posZ)
    return(pt)


def MakeClamped(x, voxelSize):
    clampedPt: rhino3dm.Point3d = rhino3dm.Point3d(math.floor(x.posX / voxelSize) * voxelSize, math.floor(x.posY / voxelSize) * voxelSize, math.floor(x.posZ / voxelSize) * voxelSize)
    return(clampedPt)



def ColumnToList(df: pd.DataFrame, i):
    quer = f'Tree == {i}'
    print(quer)
    tree = df.query(quer)
    col = tree['voxel'].tolist()
    return (col)
    

def GetTreeVoxels(pts, ptsClamped, index, isOrig):
    print('called')
    if(isOrig):
        return ColumnToList(pts, index)
    else:
        return ColumnToList(ptsClamped, index)

def CullPts(pts : List[rhino3dm.Point3d]):
    
    tups = []
    for pt in pts:
        t = (pt.X,pt.Y,pt.Z)
        tups.append(t)

    output = []
    uniquePts: List[rhino3dm.Point3d] = []

    print(f'unculled is {len(pts)}')

    for x in tups:
        if x not in output:
            output.append(x)
            uniquePt = rhino3dm.Point3d(x[0],x[1],x[2])
            uniquePts.append(uniquePt)


    print(f'culled is {len(uniquePts)}')
    return uniquePts
        


def Voxelise(index, vSize, isOrig, isCull):
    ptsClamped = data.apply(MakeClamped, args = (vSize, ), axis = 1).reset_index(name='voxel')
    #ptsClamped = data.apply((lambda x: MakeClamped(vSize))), axis = 1).reset_index(name='voxel')



    ptsClamped.set_index('Tree', inplace = True)

    pts = data.apply(MakePt, axis = 1).reset_index(name='voxel')
    pts.set_index('Tree', inplace = True)

    outs = GetTreeVoxels(pts, ptsClamped, index, isOrig)

    if isCull == False:
        return outs

    else:
        return CullPts(outs) 

