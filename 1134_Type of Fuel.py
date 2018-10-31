import sys

alcoCount = []
gasoCount = []
diselCount = []

def getInput():
    x = int(input())
    if x == 1:
        alcoCount.append(1)
    elif x == 2:
        gasoCount.append(2)
    elif x == 3:
        diselCount.append(3)
    elif x == 4:
        print('MUITO OBRIGADO')
        print('Alcool: {}'.format(len(alcoCount)))
        print('Gasolina: {}'.format(len(gasoCount)))
        print('Diesel: {}'.format(len(diselCount)))

        sys.exit(4)
    elif x > 4:
        getInput()

while True:
    x = int(input())
    if x == 1:
        alcoCount.append(1)
    elif x == 2:
        gasoCount.append(2)
    elif x == 3:
        diselCount.append(3)
    elif x == 4:
        print('MUITO OBRIGADO')
        print('Alcool: {}'.format(len(alcoCount)))
        print('Gasolina: {}'.format(len(gasoCount)))
        print('Diesel: {}'.format(len(diselCount)))
        break
    elif x > 4:
        getInput()
