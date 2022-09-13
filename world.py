from agent import Agent
from typing import List
from typing import Dict
import visualiser
import rhino3dm

agentBases: List[rhino3dm.Point3d] = []
basePool: List[rhino3dm.Point3d] = []

def PopulateBase(pts: List[rhino3dm.Point3d]):
    for pt in pts:
        agentBases.append(pt)
    basePool = agentBases.copy()
    print (f'{agentBases.count} base pts loaded')

def AssignBases(agents: List[Agent]):
    
    tempPool = basePool.copy()
    count = 0
    for pt in tempPool:
        #assign pt to agent

        del basePool[count]        
        count = count + 1

        if tempPool.count < 1:
            tempPool = basePool.copy()
    
    basePool = tempPool.copy()


def AssignBases2(agent: Agent):
    
    pt = basePool[0]
    del basePool[0]

    if basePool.count < 1:
        basePool = agentBases.copy()

    return pt

