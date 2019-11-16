rand_string = "   this is an important string   "

rand_string = rand_string.lstrip()

rand_string = rand_string.rstrip()

rand_string = rand_string.strip()

print(rand_string.capitalize())

print(rand_string.upper())

print(rand_string.lower())

a_list = ["bunch", "of", "random", "words"]
print(" ".join(a_list))

a_list2 = rand_string.split()
for i in a_list2:
    print(i)

print("How many is :", rand_string.count("is"))

print("Where is string :", rand_string.find("string"))

print(rand_string.replace("an ", "a kind of "))

