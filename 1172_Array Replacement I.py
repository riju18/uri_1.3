allNum=[]
for i in range(10):
    x=int(input())
    allNum.append(x)

for i,o in enumerate(allNum):
    if o<0 or o==0:
        o=1
    print('X[{}] = {} '.format(i, o))