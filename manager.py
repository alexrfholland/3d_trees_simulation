from http.server import CGIHTTPRequestHandler
import importer
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

    
    def doModel(self, year):
        self.LoadJSON()
        self.AssignTreePts(year)
            
    def IncreaseCount(self):
        self.count = self.count + 1

    def LoadParquet(self):
        print('starting to run model')
        df = importer.ImportParquetTrees()
        print(f'loaded {len(df)} raw trees')

        for i, row in enumerate(df.itertuples(), 1):
            print(i, row)

    
    
    def cellToAgent(self, x):
        #x is a dictionary with the agent info in it
        a = Agent()

    def LoadParquet2(self, year):  ##this would form the basis of the visualiser
        print('starting to run model')
        rawTrees = importer.ImportParquetTrees()
        print(f'loaded {len(rawTrees)} raw trees')

        treeAgents: List[Agent] = []
        treeAgents = rawTrees.applymap(self.cellToAgent)

        
        log = f'made {len(self.trees)} agents'
        self.isJSON = True
        self.IncreaseCount()
        print(log)
        return log




    def LoadJSON(self):
        print('starting to run model')
        rawTrees = importer.ImportTrees()
        print(f'loaded {len(rawTrees)} raw trees')
        count = 0

        for row in rawTrees:

            a = Agent(row, 'tree')
            self.trees.append(a)
            if(count > 10000):
                break
            count = count + 1
        
        log = f'made {len(self.trees)} agents'
        self.isJSON = True
        self.IncreaseCount()
        print(log)
        return log


    def BuildBases(self, basePts: List[rhino3dm.Point3d]):
        print('#####called build bases')
        world.PopulateBase(basePts)

        for tree in self.trees:
            tree.base = world.AssignBases2()

        print('#####finished build bases')


        self.isWorld = True
        self.IncreaseCount()
        return f'building world - finished assigning bases'
        
    def AssignTreePts(self, year):
        for tree in self.trees:
            tree.CheckandChangeTreePts(year)
            

    #currently just does trees 
    def GetResources(self, _year):
        pts = []
        treePts: List[rhino3dm.Point3d] = []
        ages = []
        perfs = []
        reses = []
        cols = []

        year = str(round(_year))

        print(f'Getting for year {year}!')
        print(f'number of agents is {len(self.trees)}')

        for agent in self.trees:
            if year in agent.age:
                ag = agent.age[year]
                perf = agent.performance[year]
                res = agent.resources[year]
                pt = agent.base
                

                ages.append(ag)
                perfs.append(perf)
                reses.append(res)
                pts.append(pt)

                #print(f'tree Pts in agent are {agent.treePts[-1]}')

                treePts.extend(agent.treePts[-1])

                col = agent.GetCols(year)

                for pt in agent.treePts[-1]:
                    cols.append(rhino3dm.Vector3d(col[0], col[1], col[2]))

        return (pts, ages, perfs, reses, cols, treePts)

    def GetPts(self, _year):
        year = str(round(_year))
        return visualiser.GetPoints2(self.trees, year)
    




