import manager
#manager.Run()
#info = manager.GetResources(3)
#print(f'Get Resource FUnction : {info}')

print('started')
manager.Run()
info = manager.GetResources(20)
#info = manager.GetPts(3)

for i in range(30):
    print(info[3][i]['low'])

print('ended')

