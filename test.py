import rhino3dm
import settings

from rhino3dm import *
import tkinter as Tkinter
import time
import compute_rhino3d.Brep


# generate random integer values
import random
from random import seed
from random import randint




#ttps://github.com/mcneel/rhino-developer-samples/blob/7/compute/py/SampleTkinter/makemesh.py

compute_rhino3d.Util.url = "http://localhost:8081/"
#compute_rhino3d.Util.apiKey = ""

def GetBase(brp: rhino3dm.Brep):
    u = random.uniform(0, 1000)/1000
    v = random.uniform(0, 1000)/1000

    srf: rhino3dm.NurbsSurface = brp.Surfaces[0]
    pt: rhino3dm.Point3d = srf.PointAt(u, v)
    isInside = compute_rhino3d.Brep.IsPointInside(brp, pt,1, False)

    print(isInside)


    return (isInside, pt)

print("starting")
path = settings.IMPORTFOLDERGEO + 'base.3dm'

model = rhino3dm.File3dm.Read(path)

brp: rhino3dm.Brep = model.Objects[0].Geometry

isInside = False
pt: rhino3dm.Point3d

while(isInside == False):
    output = GetBase(brp)
    isInside = output[0]
    pt = output
