
allAges=[]

while True:
    x=int(input())
    if x<0:
        break
    allAges.append(x)

print('{0:.2f}'.format(sum(allAges)/len(allAges)))