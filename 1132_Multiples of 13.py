x = int(input())
y = int(input())
summ = 0

if x < y:
    for i in range(x, y + 1):
        if i % 13 != 0:
            summ += i
elif x > y:
    for i in range(y, x + 1):
        if i % 13 != 0:
            summ += i
print(summ)        
