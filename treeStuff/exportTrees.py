import pandas as pd
from typing import List
from typing import Dict
import trees
import treeSettings
import rhino3dm



voxelSizes = [1,2.5,5,10]
treeIndexes = range(1,17)


tempTreeLookups = {}

for size in voxelSizes:
    treesAtThisSize = {}
    print(f'voxel size is {size}')
    for i in treeIndexes:
        #treePts = trees.Voxelise(i, size, False, True)
        treePts = trees.Tupelise(i, size)
        treesAtThisSize.update({i : treePts})
    tempTreeLookups.update({size : treesAtThisSize})

df = pd.DataFrame.from_dict(tempTreeLookups, orient='index', columns=treeIndexes)

treeLookups = df.transpose()
print(treeLookups.info())

filepath = treeSettings.IMPORTPATH + 'treeLookups.pkl'
#treeLookups.to_csv(filepath)
treeLookups.to_pickle(filepath)


