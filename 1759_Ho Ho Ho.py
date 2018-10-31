n = int(input())
x = 'ho '
result = x * n
result = result.split()
final = ''
for i in result:
    final += i + ' '

final = final[:-1]
print(final + '!')