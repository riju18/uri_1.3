allNUm=[]
for i in range(20):
    x=int(input())
    allNUm.append(x)

first10=allNUm[0:10]
first10=first10[::-1]
last10=allNUm[10:20]
last10=last10[::-1]

allNUm[0:10]=last10
allNUm[10:20]=first10
for i,o in enumerate(allNUm):
    print('N[{}] = {}'.format(i,o))