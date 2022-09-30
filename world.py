#from agent import Agent
from typing import List
from typing import Dict
import rhino3dm
import settings

# generate random integer values
import random
from random import seed
from random import randint

path = settings.IMPORTFOLDERGEO + 'base.3dm'
model = rhino3dm.File3dm.Read(path)
brp: rhino3dm.Brep = model.Objects[0].Geometry
agentBoundary: rhino3dm.NurbsSurface = brp.Surfaces[0]

def GetBase():
    u = random.uniform(200, 800)/1000
    v = random.uniform(200, 800)/1000
    pt: rhino3dm.Point3d = agentBoundary.PointAt(u, v)
    return pt


"""agentBases: List[rhino3dm.Point3d] = []
basePool: List[rhino3dm.Point3d] = []

def PopulateBase(pts: List[rhino3dm.Point3d]):
    global basePool
    for pt in pts:
        agentBases.append(pt)
    basePool = agentBases.copy()
    print (f'{agentBases.count} base pts loaded')


def AssignBases2():
    global basePool
    _pt = basePool[0]
    pt = rhino3dm.Point3d(_pt.X,_pt.Y,_pt.Z)

    del basePool[0]

    if len(basePool) < 1:
        basePool = agentBases.copy()

    return pt"""

