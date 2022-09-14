import rhino3dm

import random

# generate random integer values
from random import seed
from random import randint


class Agent:
    age = {}
    performance = {}
    resources = {}

    def __init__(self, info, _kind):
        self.age = info['age']
        self.performance = info['performance']
        self.resources = info['resources']
        self.kind = _kind

        self.GetPoint()

    def Test(self):
        #print(f'{self.age} {self.kind} {self.resources} {self.performance}')
        print(f'ages are {self.age}')

    
    def GetPoint(self):
        x = random.uniform(0, 100)
        y = random.uniform(0, 100)
        self.point = rhino3dm.Point3d(x, y, 0)




