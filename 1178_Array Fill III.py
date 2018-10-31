x = float(input())
size = []
allNum = []
for i in range(100):
    size.append(i)

for i, o in enumerate(size):
    x = x / 2
    allNum.append(x)

for i, o in enumerate(allNum):
    print('N[{}] = {:.4f}'.format(i, o * 2))


