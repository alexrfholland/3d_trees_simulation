import pandas as pd
import settings as set
import json
import dictor
import settings as set

import json
from dictor import dictor

import rhino3dm


def ImportTrees():
    path = set.IMPORTWINDOW2 + 'json//trees.json'
    with open(path) as data: 
        data = json.load(data)
        return(data)

def ImportPandaTrees():
    path = set.IMPORTWINDOWS + 'treeDF.pk1'
    df = pd.read_pickle(path)
    return df

def ImportParquetTrees():
    path = set.IMPORTWINDOWS + 'treeDF.parquet'
    df = pd.read_parquet(path, engine='fastparquet')
    return df

def ImportParquetSelectTreeYrs(year):
    col = f'y{int(year)}'
    print(f'importing trees from {col}')
    path = set.IMPORTWINDOWS + 'treeDF.parquet'
    df = pd.read_parquet(path, engine='fastparquet', columns = [col])
    return df


def LoadParquet():
    print('starting to run model')
    df = ImportParquetTrees()
    #delete first irrelevant column so columns represent years
    #df.drop([df.columns[0]], axis = 1)
    print(f'loaded {len(df)} raw trees')

    
    #convert a list of agents to a row

    print(len(df.index))
    print(df)

    #this gets every row, each row is an agent, each column is a year, each cell describes the stats of an agent for that year
    #the output is a list per agent where each element is the values for that year
    for i in range(len(df.index)):
        rowList = df.loc[i, :].values.flatten().tolist()

        #agent stats
        perf = {}
        age = {}
        isAlive = {}
        res = {}
        print("new agent")

        for year in range(len(rowList)):
            cell = rowList[year]
            print(cell)

           
        
            




    
    """#this gets every row, each row is an agent, each column is a year, each cell describes the stats of an agent for that year
    for i, row in enumerate(df.itertuples(), 1):
        print(i, row[30])

        rowList = df.loc[0, :].values.tolist()
        print(rowList)

        #assemble an agent from a row
        cols = len(row)
        
        perf = {}
        age = {}
        isAlive = {}
        res = {}

        #each column is a year stats, convert cells into a nested dictionary where the first level is:
        #
        for col in range(cols):
            #the year is col -1 as there is a header column
            year = col -1
            rowList = row.values.flatten().tolist()
            print(rowList[0])
            print(f'row is {rowList}')
            print(f'cell is {cell}')
            perf.update({year : cell["performance"]})
            age.update({year : cell["age"]})
            isAlive.update({year : cell["alive"]})
            res.update({year : ["resources"]})

        info = {'performance' : perf,
                'age' : age,
                'tree-status' : isAlive,
                'resources' : res
                }
        print(info)
        """
    