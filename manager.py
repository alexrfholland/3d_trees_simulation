from http.server import CGIHTTPRequestHandler
import jsonImporter
from agent import Agent
from typing import List
from typing import Dict
import visualiser
import world
import rhino3dm

class Model:

    trees: List[Agent] = []
    isInit = False
    isJSON = False
    isWorld = False
    count = 0


    def __init__(self):
        self.isInit = True
        self.IncreaseCount()
        
    def IncreaseCount(self):
        self.count = self.count + 1

    def LoadJSON(self):
        print('starting to run model')
        rawTrees = jsonImporter.ImportTrees()
        print(f'loaded {len(rawTrees)} raw trees')

        for row in rawTrees:
            a = Agent(row, 'tree')
            self.trees.append(a)
        
        log = f'made {len(self.trees)} agents'
        self.isJSON = True
        self.IncreaseCount()
        print(log)
        return log


    def BuildBases(self, basePts: List[rhino3dm.Point3d]):
        print('#####called build bases')
        world.PopulateBase(basePts)

        for tree in self.trees:
            tree.point = world.AssignBases2()

        print('#####finished build bases')


        self.isWorld = True
        self.IncreaseCount()
        return f'building world - finished assigning bases'
        
    #currently just does trees 
    def GetResources(self, _year):
        pts = []
        ages = []
        perfs = []
        reses = []

        year = str(round(_year))

        print(f'Getting for year {year}!')
        print(f'number of agents is {len(self.trees)}')

        for agent in self.trees:

            ag = agent.age[year]
            perf = agent.performance[year]
            res = agent.resources[year]
            pt = agent.point

            ages.append(ag)
            perfs.append(perf)
            reses.append(res)
            pts.append(pt)

            print(pt)

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

    def GetPts(self, _year):
        year = str(round(_year))
        return visualiser.GetPoints2(self.trees, year)
    




