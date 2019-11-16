import random
import math

# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of
#    the list when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning
#    of the loop
# 4. Check if list[Index] > list[Index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at
#    the end of the list
# 7. Decrement the outer loop by 1

numList = []

for i in range(5):
    numList.append(random.randrange(1, 10))

for k in numList:
    print(k, end=", ")

i = len(numList) - 1

while i:

    j = 0

    while j < i:

        print("\nIs {} > {}".format(numList[j], numList[j + 1]))

        if numList[j] < numList[j + 1]:

            print("Switch")

            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print("No Switch")

        j += 1

        for k in numList:
            print(k, end=", ")
        print()

    print("***End Of Cycle***")

    i -= 1


for k in numList:
    print(k, end=", ")

print()