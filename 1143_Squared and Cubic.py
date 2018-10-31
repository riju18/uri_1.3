x = int(input())
def result(i):
    print('{} {} {}'.format(i, i ** 2, i ** 3))

for i in range(1, x + 1):
    result(i)
