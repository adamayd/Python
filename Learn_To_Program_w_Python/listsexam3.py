import random
import math

multList = [[0] * 9 for i in range(9)]

for i in range(1,10):

    for j in range(1, 10):

        multList[i-1][j-1] = i * j

for i in range(9):

    for j in range(9):

        print(multList[i][j], end=", ")

    print()