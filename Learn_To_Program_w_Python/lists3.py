import random
import math

numList = []
for i in range(5):
    numList.append(random.randrange(1, 10))

numList.sort()
for k in numList:
    print(k, end=", ")
print()

numList.reverse()
for k in numList:
    print(k, end=", ")
print()

numList.insert(3, 10)
for k in numList:
    print(k, end=", ")
print()

numList.remove(10)
for k in numList:
    print(k, end=", ")
print()

numList.pop(2)
for k in numList:
    print(k, end=", ")
print()

