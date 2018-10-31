inputs = str(input())
split = inputs.split()
inInt = list(map(int, split))
x = inInt[0]
y = inInt[1]

for i in range(1, y + 1):
    print(i, end=' ')
    if i % x == 0:
        print()