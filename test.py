import rhino3dm

pA = rhino3dm.Point3d(0,0,0)
pB = rhino3dm.Point3d(0,0,0)
pC = rhino3dm.Point3d(3,0,0)
 

if pA == pB:
    print('pA equals pB')
else:
    print('pA !equals pB')

if pA == pC:
    print('pA equals pC')
else:
    print('pA equals pC')
