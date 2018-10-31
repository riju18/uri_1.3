allNum=[]

for i in range(100):
    x=float(input())
    allNum.append(x)

for i,o in enumerate(allNum):
    if o==10 or o<10:
        print('A[{}] = {}'.format(i,o))