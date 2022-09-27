import pandas as pd
from typing import List
from typing import Dict
import rhino3dm
import settings as set
import random

importPath = 'C:\\Users\\alexholland\\OneDrive - The University of Melbourne\\_PhD Private\\Source FIles\\Chapter 3 Briefs\\Sim\\data\\trees\\'


#filepath = treeSettings.IMPORTPATH + 'treeLookups.pkl'

filepath = importPath + 'treeLookups.pkl'

df = pd.read_pickle(filepath)


def MakePt(x):
    pts: List[rhino3dm.Point3d] = []
    ptList: rhino3dm.Point3dList = rhino3dm.Point3dList()
    
    for i in x:
        #print(f'i is {i}')
        pt: rhino3dm.Point3d = rhino3dm.Point3d(i[0],i[1],i[2])
        pts.append(pt)
        ptList.Add(pt.X,pt.Y,pt.Z)
    #return(pts)# return list of points
    return(ptList) # return rhino 'pointlist' collection of points

pts = df.applymap(MakePt)
print(pts)

def getPts(tree):
    treePts: List[rhino3dm.Point3d] = pts.iloc[tree,set.VOXELLEVEL]
    return treePts

print(f'imported trees')
#print(pts)



#pts = df.apply(MakePt, axis = 1).reset_index(name='pt')
#pts.set_index('Tree', inplace = True)
