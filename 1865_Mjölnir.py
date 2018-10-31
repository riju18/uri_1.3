tesecase = int(input())
allHammers = []
for i in range(tesecase):
    liftHammer = str(input())
    split = liftHammer.split()
    allHammers.append(split)

for i in range(len(allHammers)):
    allHammers[i][1] = int(allHammers[i][1])
    if allHammers[i][0] == 'Thor':
        print('Y')
    else:
        print('N')