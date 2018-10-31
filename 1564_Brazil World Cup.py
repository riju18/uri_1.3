complaints = []

while True:
    x = (input())
    if x == '':
        break
    complaints.append(x)

complaints = list(map(int, complaints))
for i in complaints:
    if i == 0:
        print('vai ter copa!')
    elif i > 0:
        print('vai ter duas!')
