allNum=[]
while True:
    x=int(input())
    if x==0:
        break
    else:
        allNum.append(x)

def result(i):
    for m in range(1, i+1):
        print('{}'.format(m), end=' ')

for i in allNum:
    result(i)
    print('\n')