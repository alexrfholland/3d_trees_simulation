from http.server import CGIHTTPRequestHandler
import importer
from agent import Agent
from typing import List
from typing import Dict
import visualiser
import world
import rhino3dm
from codetiming import Timer
from tabulate import tabulate


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
        print('starting to run model')
        #self.LoadJSON()
        df = importer.LoadParquet()
        print('calling get agent infos')
        agentInfos = importer.GetCells(df)
        print('calling make agents')
        self.trees = importer.ConvertToAgents(agentInfos)
        print(f'made {len(self.trees)} trees')
        print('calling assigning trees')
        self.AssignPts(year)
        self.GetSummaries(year)
            

    @Timer()
    def AssignPts(self, year):
        print('assigning 3d points')
        count = 0
        for tree in self.trees:
            count = count + 1
            tree.CheckandChangeTreePts(year)
        print(f'assigned 3d points to {count} agents')
    
    
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
        
    @Timer
    def AssignTreePts(self, year):
        print('test')
        """print(f'assigning 3d points to {len(self.trees)} agents')
        for tree in self.trees:
            tree.CheckandChangeTreePts(year)
        print('assigned 3d points')"""
    
    

    #currently just does trees 
    def GetResources(self, _year):
        pts = []
        treePts: List[rhino3dm.Point3d] = []
        ages = []
        perfs = []
        reses = []
        cols = []

        year = _year

        print(f'Getting resources for year {year}!')
        #print(f'number of agents is {len(self.trees)}')

        count = 0

        for agent in self.trees:
            #print(f'agent age is {agent.age}')
            if agent.isAlive[year] == True:
                count = count + 1
                ag = agent.age[year]
                perf = agent.performance[year]
                res = agent.resources[year]
                pt = agent.base
                

                ages.append(ag)
                perfs.append(perf)
                reses.append(res)
                pts.append(pt)

                #print(f'tree Pts in agent are {agent.treePts[-1]}')

                treePts.extend(agent.treePts[agent.ag])

                col = agent.GetCols(year)

                for pt in agent.treePts[agent.ag]:
                    cols.append(rhino3dm.Vector3d(col[0], col[1], col[2]))

        print(f'added {count} agent stats')
        return (pts, ages, perfs, reses, cols, treePts)

    def GetSummaries(self, year):
        
        print(f'getting summaries for {year}')
        res = ['low', 'medium', 'high', 'total', 'dead', 'lateral']
        ages = ['small', 'med', 'large']
        
        summaries = {}
        agentsAlive = 0


        for resName in res:
            summaries.update({resName : 0})

        for agName in ages:
            summaries.update({agName : 0})
        
        for agent in self.trees:
            if agent.isAlive[year]:
                agentsAlive = agentsAlive + 1
                summaries[agent.ag] = summaries[agent.ag] + 1
                for resName in res:
                    if agent.resources[year][resName] > summaries[resName]:
                        summaries[resName] = round(agent.resources[year][resName])
                

        summaries.update({'agents alive' : agentsAlive})

        print(f'summaries are {summaries}')
       


    def GetPts(self, _year):
        year = str(round(_year))
        return visualiser.GetPoints2(self.trees, year)
    




