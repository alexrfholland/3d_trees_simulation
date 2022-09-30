import rhino3dm
from agent import Agent
from typing import List


def GetPoints(agents: List[Agent], year):

    visuals = rhino3dm.PointCloud()
   
    for agent in agents:
        val = agent.resources[year]["medium"]
        val2 = remap(val, 0, 50, 0, 10)

        for i in range(val2):
            pt = rhino3dm.Point3d(agent.base.X, i, agent.base.Z)      
            visuals.Add(pt)

    return visuals

def GetPoints2(agents: List[Agent], year):

    pts: List[rhino3dm.Point3d] = []
    
    for agent in agents:
        val = agent.resources[year]["medium"]
        val2 = remap(val, 0, 50, 0, 10)

        for i in range(round(val2)):
            pt = rhino3dm.Point3d(agent.base.X, i, agent.base.Z)      
            pts.append(pt)

    return pts

def remap( x, oMin, oMax, nMin, nMax ):

    #range check
    if oMin == oMax:
        print ("Warning: Zero input range")
        return None

    if nMin == nMax:
        print ("Warning: Zero output range")
        return None

    #check reversed input range
    reverseInput = False
    oldMin = min( oMin, oMax )
    oldMax = max( oMin, oMax )
    if not oldMin == oMin:
        reverseInput = True

    #check reversed output range
    reverseOutput = False   
    newMin = min( nMin, nMax )
    newMax = max( nMin, nMax )
    if not newMin == nMin :
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result

