import numpy as np

x = int(input())
rangee = np.arange(1, x + 1)

def result(i):
    if i % 2 != 0:
        print('{} {} {} PUM'.format((i ** 2), (i ** 2 + 1), (i ** 2 + 2)))
    elif i % 2 == 0:
        print('{} {} {} PUM'.format((i ** 2 + 1), (i ** 2 + 2), (i ** 2 + 3)))
        
for i in rangee:
    result(i)

## **  did not match 100% with sample data  **