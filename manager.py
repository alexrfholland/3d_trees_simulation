from http.server import CGIHTTPRequestHandler
import jsonImporter
from agent import Agent
from typing import List
from typing import Dict
import visualiser
import world
import rhino3dm

trees: List[Agent] = []
hello = 5

def Run():
    global hello
    hello = 2
    print('starting to run model')
    rawTrees = jsonImporter.ImportTrees()
    print(f'loaded {len(rawTrees)} raw trees')

    for row in rawTrees:
        a = Agent(row, 'tree')
        trees.append(a)
    
    log = f'made {len(trees)} agents'
    print(log)
    return log


def BuildBases(basePts: List[rhino3dm.Point3d]):
    world.PopulateBase(basePts)

    for tree in trees:
        tree.point = world.AssignBases2(tree)

    return f'building world - finished assigning bases'
    
#currently just does trees 
def GetResources(_year):
    pts = []
    ages = []
    perfs = []
    reses = []

    year = str(round(_year))

    print(f'Getting for year {year}!')
    print(f'number of agents is {len(trees)}')

    for agent in trees:

        ag = agent.age[year]
        perf = agent.performance[year]
        res = agent.resources[year]
        pt = agent.point

        ages.append(ag)
        perfs.append(perf)
        reses.append(res)
        pts.append(pt)

        if "year" in agent.age:
            ag = agent.age[year]
            perf = agent.performance[year]
            res = agent.resources[year]
            pt = agent.point

            ages.append(ag)
            perfs.append(perf)
            reses.append(res)
            pts.append(pt)


    return (pts, ages, perfs, reses)

def GetPts(_year):
    year = str(round(_year))
    return visualiser.GetPoints2(trees, year)
    




