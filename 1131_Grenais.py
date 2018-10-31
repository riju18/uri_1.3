allGoals = []

def result():
    interCount = 0
    gremioCount = 0
    drawCount = 0

    for i in range(len(allGoals)):
        inter = allGoals[i][0]
        gremio = allGoals[i][1]
        if inter > gremio:
            interCount += 1
        elif gremio > inter:
            gremioCount += 1
        elif inter == gremio:
            drawCount += 1
    print('{} grenais'.format(len(allGoals)))
    print('Inter:{}'.format(interCount))
    print('Gremio:{}'.format(gremioCount))
    print('Empates:{}'.format(drawCount))
    if interCount > gremioCount:
        print('Inter venceu mais')
    elif gremioCount > interCount:
        print('Gremio venceu mais')
    elif interCount == gremioCount:
        print('Nao houve vencedor')

def getInput():
    goals = str(input())
    split = goals.split()
    inInt = list(map(int, split))
    allGoals.append(inInt)
    x = int(input())
    if x == 1:
        print('Novo grenal (1-sim 2-nao)')
        getInput()
    elif x == 2:
        result()
        return False

while True:
    print('Novo grenal (1-sim 2-nao)')
    x = getInput()
    if not x:
        break
