x = int(input())
allNum = []
for i in range(x):
    inputs = str(input())
    split = inputs.split()
    inInt = list(map(int, split))
    allNum.append(inInt)
for i in allNum:
    result = sum(i)
    print(result)