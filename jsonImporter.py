import pandas as pd
import settings as set
import json
import dictor

import json
from dictor import dictor

import rhino3dm


def ImportTrees():
    path = set.IMPORTFOLDER + 'trees.json'
    with open(path) as data: 
        data = json.load(data)
        return(data)
 