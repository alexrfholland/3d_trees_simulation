import rhino3dm

import random
import math

import treeStuff.importTrees as trees
#import treeStuff.treeSettings as tSettings
import settings as tSettings


from typing import List
from typing import Dict

# generate random integer values
from random import seed
from random import randint

import settings as set

import world

import helpers

useWorld = True


class Agent:

    def __init__(self, info, _kind):
        self.age = info['age']
        self.performance = info['performance']
        self.resources = info['resources'].copy()
        self.isAlive = info['isAlive']
        #self.alive = info['tree-status']
        self.kind = _kind

        self.treeIndexes = {}
        self.ageThresholds = {}
        #self.pts: List[rhino3dm.Point3dList] = [] ##maybe convert this to dictionary
        #self.treePts: List[List[rhino3dm.Point3d]] = [[]] ##maybe convert this to dictionary
        self.treePts: Dict[str, List[rhino3dm.Point3d]] = {} ##maybe convert this to dictionary

        self.test = []
        self.ag = 'unassigned'

        self.GetPoint()
        self.GetTreeIndexesAndThresholds()


    def GetPoint(self):
        if(useWorld):
            self.base = world.GetBase()
        else:
            x = random.uniform(0, 10000)
            y = random.uniform(0, 10000)
            self.base = rhino3dm.Point3d(x, y, 0)

    def GetTreeIndexesAndThresholds(self):
        s = random.choice(tSettings.YOUNG)
        m = random.choice(tSettings.MEDIUM)
        l = random.choice(tSettings.OLD)

        mL = random.choice(tSettings.MDBH)
        oL = random.choice(tSettings.ODBH)

        #self.treeIndexes = [s,m,l]
        self.treeIndexes = {'small' : s, 'medium' : m, 'large' : l}
        #self.ageThresholds = [mL, oL]
        self.ageThresholds = {'medium' : mL, 'large' : oL}

    def  CheckandChangeTreePts(self, _year):
    
        #print('check is called')
        #year = str(_year)
        year = _year

        if len(self.treePts) > 0:
            print(f'length of treepts are {len(self.treePts)} and keys are {self.treePts.keys}')

    
        #age thresholds are...

        if self.performance[year] < self.ageThresholds['medium']:

            self.ag = 'small'
            skipped = True
            #print( 'young tree and treePts are {len(self.treePts)}')

            #check if pts have been updated...
            if(len(self.treePts) < 1):

                _pts: rhino3dm.Point3dList = trees.getPts(self.treeIndexes['small'])
                #print(f'points are {_pts}')

                self.treePts.update({self.ag: self.TransformTree(_pts)})

                skipped = False

            
        elif self.performance[year] < self.ageThresholds['large']:
            
            self.ag = 'med'
            #check if pts have been updated...
            if(len(self.treePts) < 2):
                _pts: rhino3dm.Point3dList = trees.getPts(self.treeIndexes['medium'])          
                self.treePts.update({self.ag : self.TransformTree(_pts)})
                skipped = False


        else: 
            #print("tree is old")
            #check if pts have been updated...
            self.ag = 'large'
            if(len(self.treePts) < 3):
                _pts: rhino3dm.Point3dList = trees.getPts(self.treeIndexes['large'])
                self.treePts.update({self.ag : self.TransformTree(_pts)})
                skipped = False
        
        
        #print(f'Tree pts are {self.treePts[-1]}')
        if(skipped):
            print(f'skipped this tree c;assified as {self.ag} and length of treePts is {len(self.treePts)} and age thresholds are {self.ageThresholds}')


    def TransformTree(self, _pts: rhino3dm.Point3dList):
        trans = rhino3dm.Transform.Translation(self.base.X, self.base.Y, self.base.Z)

        #_pts.Transform(trans)

        #newPts: rhino3dm.Point3dList = rhino3dm.Point3dList()
        newPts: List[rhino3dm.Point3d] = []


        for pt in _pts:
            #newPts.Add(pt.X,pt.Y,pt.Z)
            _pt = rhino3dm.Point3d(pt.X + self.base.X, pt.Y + self.base.Y, pt.Z + self.base.Z + 10)
            #_pt = rhino3dm.Point3d(pt.X, pt.Y, pt.Z)
            newPts.append(_pt)

        #print (f'new tree pts are {newPts}')


        return newPts

    def GetCols(self, year):
        c = [(255,255,229), (247,252,185), (217,240,163), (173,221,142), (120,198,121), (65,171,93), (35,132,67), (0,104,55), (0,69,41)]
        #i = random.randrange(len(c)-1)
        
        resource = 'high'

        """cDic = {'small' : c[0], 'med' : c[3], 'large' : c[-1]}

        c = cDic[self.ag]"""


        i = round(helpers.remap(self.resources[year][resource], 0, 30, 0, len(c) - 1))

        """ if i > len(c) - 1:
            i = len(c) - 1"""

        #print(f'{resource} is {self.resources[year][resource]} and i is {i}')


        #i = round(helpers.remap(self.age[year], 0, 29, 0, 8))

        
        #print(f'col index is {i}, {resource} is {self.resources[year][resource]}')
        return c[i]
        #return c
        #print(f'col is {self.color}')

        


       
        


    




