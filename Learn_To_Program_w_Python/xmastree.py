rows = eval(input('Enter how many rows for your tree: '))
hashes = 1
spaces = rows - 1
r = 0

while r != rows:
    s = 1
    for s in range(spaces):
        print(' ', end="")

    h = hashes - 1
    for h in range(hashes):
        print('#', end="")

    print()
    spaces -= 1
    hashes += 2
    r += 1

s = 1
for s in range(rows - 1):
    print(' ', end="")

print('#')


# print(' ', end="")
# print('#', end="")
