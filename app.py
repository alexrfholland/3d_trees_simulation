"""Hops flask middleware example"""
from calendar import c
from itertools import count
from flask import Flask
import ghhops_server as hs
import rhino3dm
import manager
from typing import List
from datetime import *



# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"

##model stuff
manager.Run()


@hops.component(
    "/binmult",
    inputs=[hs.HopsNumber("A"), hs.HopsNumber("B")],
    outputs=[hs.HopsNumber("Multiply")],
)
def BinaryMultiply(a: float, b: float):
    return a * b

    
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
        'hi'
    #manager.Run  
    #message = f'loaded {len(manager.trees)} trees {manager.hello}'
    

    log = f'{message} at {timestamp}'

    return log


@hops.component(
    "/loadWorld",
    name="world",
    nickname="world",
    description="world",
    icon="pointat.png",
    inputs=[
        hs.HopsBoolean("Toggle", "T", "Evaluate Function"),
        hs.HopsPoint("bases", "bases", "bases", access= hs.HopsParamAccess.TREE)
    ],
    outputs=
    [hs.HopsString("L", "L", "log")
    ]
)
def loadWorld(toggle, bases):
    
    message = "Not Loaded 3"
    if toggle:
        my_list = list(bases.values())

        timestamp = datetime.now().strftime("%H-%M-%S")

        message = f'loaded {len(my_list)} bases at {timestamp}'



        #manager.BuildBases(my_list)
    return message


@hops.component(
    "/getAgents",
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
def getAgents(y=0):
    info = manager.GetResources(y)
    return (info[0])


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
