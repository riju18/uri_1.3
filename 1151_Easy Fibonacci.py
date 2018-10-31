x = int(input())
fiboList = []
result = ''
def easy_fibo(i):
    if i <= 1:
        return i
    else:
        return (easy_fibo(i - 1) + easy_fibo(i - 2))
for i in range(x):
    fiboList.append(easy_fibo(i))
for i in fiboList:
    result += str(i) + ' '
print(result[:-1])
