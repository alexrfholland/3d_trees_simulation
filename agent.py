import rhino3dm

import random

import treeStuff.importTrees as trees
#import treeStuff.treeSettings as tSettings
import settings as tSettings


from typing import List
from typing import Dict

# generate random integer values
from random import seed
from random import randint

import settings as set

class Agent:
    


    def __init__(self, info, _kind):
        self.age = info['age']
        self.performance = info['performance']
        self.resources = info['resources']
        self.kind = _kind

        self.treeIndexes = {}
        self.ageThresholds = {}
        #self.pts: List[rhino3dm.Point3dList] = [] ##maybe convert this to dictionary
        self.treePts: List[List[rhino3dm.Point3d]] = [[]] ##maybe convert this to dictionary

        self.test = []

        self.GetPoint()
        self.GetTreeIndexesAndThresholds()

    def Test(self):
        #print(f'{self.age} {self.kind} {self.resources} {self.performance}')
        print(f'ages are {self.age}')

    
    def GetPoint(self):
        x = random.uniform(0, 100)
        y = random.uniform(0, 100)
        self.point = rhino3dm.Point3d(x, y, 0)


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

    def CheckandChangeTreePts(self, _year):
    
        year = str(_year)

        #age thresholds are...

        if self.performance[year] < self.ageThresholds['medium']:
             #check if pts have been updated...
            if(len(self.treePts) < 1):

                _pts: rhino3dm.Point3dList = trees.getPts(self.treeIndexes['small'])

                self.treePts.append(self.TransformTree(_pts))

            
        elif self.performance[year] < self.ageThresholds['large']:
            #check if pts have been updated...
            if(len(self.treePts) < 2):
                _pts: rhino3dm.Point3dList = trees.getPts(self.treeIndexes['medium'])          
                self.treePts.append(self.TransformTree(_pts))


        else: 
            #print("tree is old")
            #check if pts have been updated...
            if(len(self.treePts) < 3):
                _pts: rhino3dm.Point3dList = trees.getPts(self.treeIndexes['large'])
                self.treePts.append(self.TransformTree(_pts))

    def TransformTree(self, _pts: rhino3dm.Point3dList):
        trans = rhino3dm.Transform.Translation(self.point.X, self.point.Y, self.point.Z)

        _pts.Transform(trans)

        #newPts: rhino3dm.Point3dList = rhino3dm.Point3dList()
        newPts: List[rhino3dm.Point3d] = []


        for pt in _pts:
            #newPts.Add(pt.X,pt.Y,pt.Z)
            _pt = rhino3dm.Point3d(pt.X,pt.Y,pt.Z)
            newPts.append(_pt)

        print (f'new tree pts are {newPts}')


        return newPts

       
        


    




