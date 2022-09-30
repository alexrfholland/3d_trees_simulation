"""Hops flask middleware example"""
from calendar import c
from itertools import count
from flask import Flask
import ghhops_server as hs
import rhino3dm
import manager
from typing import List
from datetime import *
import treeStuff.trees as trees

# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)

# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"

##model stuff
#model: manager.Model = manager.Model()

@hops.component(
    "/binmult",
    inputs=[hs.HopsNumber("A"), hs.HopsNumber("B")],
    outputs=[hs.HopsNumber("Multiply")],
)
def BinaryMultiply(a: float, b: float):
    return a * b

#Follow up with the repo: list works for lines but not points, ie, https://github.com/mcneel/compute.rhino3d/issues/316


@hops.component(
    "/Model2",
    name="agents",
    nickname="agents",
    description="Get agets",
    icon="pointat.png",
    inputs=[
        hs.HopsInteger("y", "y", "Year")
    ],
    outputs=
    [hs.HopsPoint("P", "P", "points"),
    hs.HopsPoint("B", "B", "points"),
    hs.HopsVector("C","c","colors")
    ]
)
def getAgentsb(year):
    model: manager.Model = manager.Model()
    model.doModel(year)
    res = model.GetResources(year)
    return (res[-1], res[0], res[-2])


@hops.component(
    "/surfacerandpt",
    name="agents",
    nickname="agents",
    description="Get agets",
    icon="pointat.png",
    inputs=[
        hs.HopsSurface("y", "y", "Year")
    ],
    outputs=
    [hs.HopsPoint("P", "P", "Point on curve at t")
    ]
)
def getAgentsb(surf : rhino3dm.NurbsSurface):
    pt: rhino3dm.Point3d = surf.PointAt(.5,.5)
    return (pt)

@hops.component(
    "/makeTrees",
    name="trees",
    nickname="trees",
    description="trees",
    icon="pointat.png",
    inputs=[
        hs.HopsPoint("p","p","p"),
        hs.HopsInteger("i", "i", "i"),
        hs.HopsInteger("s", "s", "s"),
        hs.HopsBoolean("isOrg","b","b"),
        hs.HopsBoolean("isCull","b","b")

    ],
    outputs=[
        hs.HopsPoint("tree", "tree", "tree")
    ]
)
def makeTrees(point, i, s, isOrig, isCull):
    return trees.Voxelise(i, s, isOrig, isCull)
    
@hops.component(
    "/startModel",
    name="model",
    nickname="model",
    description="model agets",
    icon="pointat.png",
    inputs=[
        hs.HopsBoolean("Toggle", "T", "Evaluate Function"),
        hs.HopsPoint("p","p","p")
    ],
     outputs=
    [hs.HopsString("L", "L", "log")
    ]
)
def startModel(toggle, pt):

    timestamp = datetime.now().strftime("%H-%M-%S")

    message = 'not loaded'
    if toggle:
        model.LoadJSON()
        message = f'loaded {len(model.trees)} trees and isJSON is {model.isJSON}'

    #manager.Run  
    
    log = f'{message} at {timestamp}, count is {model.count}'

    return log

@hops.component(
    "/loadWorld",
    name="world",
    nickname="world",
    description="world",
    icon="pointat.png",
    inputs=[
        hs.HopsBoolean("Toggle", "T", "Evaluate Function"),
        hs.HopsPoint("p","p","p"),
        hs.HopsLine("bases", "bases", "bases", access= hs.HopsParamAccess.LIST)
    ],
    outputs=[
        hs.HopsString("L", "L", "log")
    ]
)
def loadWorld(toggle, updater, bases: rhino3dm.Line):
    update = updater
    message = "Not Loaded "
    if toggle:
        message = "No Agents"
        if model.isJSON:
            points = [line.PointAt(0) for line in bases]
            message = f'loaded {len(points)}'
            model.BuildBases(points)
    
    timestamp = datetime.now().strftime("%H-%M-%S")
    log = f'{message} at {timestamp}, count is {model.count}'
    return log


@hops.component(
    "/loadWorld2",
    name="world",
    nickname="world",
    description="world",
    icon="pointat.png",
    inputs=[
        hs.HopsBoolean("Toggle", "T", "Evaluate Function"),
        hs.HopsPoint("p","p","p"),
        hs.HopsPoint("bases", "bases", "bases", access= hs.HopsParamAccess.LIST)
    ],
    outputs=[
        hs.HopsString("L", "L", "log")
    ]
)
def loadWorld(toggle, updater, bases):
    update = updater
    message = "Not Loaded "
    if toggle:
        message = "No Agents"
        if model.isJSON:
            my_list = [pt for pt in bases]
            #my_list = list(bases.values())
            message = f'loaded {len(my_list)}'
            model.BuildBases(my_list)
    
    timestamp = datetime.now().strftime("%H-%M-%S")
    log = f'{message} at {timestamp}, count is {model.count}'
    return log


@hops.component(
    "/getAgents",
    name="agents",
    nickname="agents",
    description="Get agets",
    icon="pointat.png",
    inputs=[
        hs.HopsBoolean("Toggle", "T", "Evaluate Function"),
        hs.HopsPoint("p","p","p"),
        hs.HopsInteger("y", "y", "Year")
    ],
    outputs=[   
        hs.HopsPoint("P", "P", "Point on curve at t", access = hs.HopsParamAccess.LIST),
        hs.HopsString("L", "L", "log")
    ]
)
def getAgents(toggle, updater, y=0):
    if toggle:
        model.AssignTreePts(y)
        info = model.GetResources(y)
        timestamp = datetime.now().strftime("%H-%M-%S")
        log = f'{timestamp}: isInit is {model.isInit}, isJSON is {model.isJSON}, isWorld is {model.isWorld}'
        #return (info[0], log)
        return (info[4], log)
    else:
        log = f'{timestamp}: not loaded'
        pt = rhino3dm.Point3d(-1,-1,-1)
        return (pt, log)


@hops.component(
    "/getAgentsb",
    name="agents",
    nickname="agents",
    description="Get agets",
    icon="pointat.png",
    inputs=[
        hs.HopsInteger("y", "y", "Year")
    ],
    outputs=
    [hs.HopsPoint("P", "P", "Point on curve at t")
    ]
)
def getAgentsb(y=0):
    info = manager.GetResources(y)
    return (info[0])


@hops.component(
    "/getAgents2",
    name="agents",
    nickname="agents",
    description="Get agets",
    icon="pointat.png",
    inputs=[
        hs.HopsInteger("y", "y", "Year")
    ],
    outputs=
    [hs.HopsPoint("P", "P", "Point on curve at t"),
    hs.HopsNumber("m", "M", "medium resources")
    ]
)
def getAgents2(y=0):
    info = manager.GetResources(y)
    print(f'points returned size {info.count}')
    res = info[3]
    mediums = [d['total'] for d in res]
    return (info[0], mediums)

@hops.component(
    "/getAgents3",
    name="agents",
    nickname="agents",
    description="Get agets",
    icon="pointat.png",
    inputs=[
        hs.HopsInteger("y", "y", "Year"),
        hs.HopsString("r","r", "Resource")
    ],
    outputs=
    [hs.HopsPoint("P", "P", "Point on curve at t"),
    hs.HopsNumber("m", "M", "medium resources")
    ]
)
def getAgents3(y: int, r: str):
    info = manager.GetResources(y)
    print(f'points returned size {info.count}')
    res = info[3]
    mediums = [d[r] for d in res]
    return (info[0], mediums)



@hops.component(
    "/getAgentPtCloud",
    name="agentsCld",
    nickname="agentsCld",
    description="Get agets",
    icon="pointat.png",
    inputs=[
        hs.HopsInteger("y", "y", "Year")
    ],
     outputs=
    [hs.HopsPoint("P", "P", "Point on curve at t"),
    ]
)
def getAgentPtCloud(y=0):
    pts = manager.GetPts(y)
    print(f'points returned size {pts.count}')
    return pts



@hops.component(
    "/add",
    name="Add",
    nickname="Add",
    description="Add numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Sum", "S", "A + B")]
)
def add(a: float, b: float):
    return a + b


@hops.component(
    "/pointatPenis",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("P", "P", "Penis"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)




@hops.component(
    "/pointat",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)


@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def ruled_surface(a: rhino3dm.Point3d,
                  b: rhino3dm.Point3d,
                  c: rhino3dm.Point3d,
                  d: rhino3dm.Point3d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)


if __name__ == "__main__":
    app.run(debug=True)
