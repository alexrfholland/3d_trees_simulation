from agent import Agent
from typing import List
from typing import Dict
import visualiser
import rhino3dm

agentBases: List[rhino3dm.Point3d] = []
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

    return pt

