x=int(input())
count=0
numbers=[]
size=[]
for i in range(x):
    numbers.append(i)

for i in range(100):
    size.append(i)

size[0]=numbers[0]
size[1]=numbers[1]
numbers[2]=numbers[2]
for i in size:
    print(size[0])
    print(size[1])
    print(size[2])
    count+=1

print(count)

# did not match with the sample
# ------------------------------