secret_string = str(input("Enter a Secret Word in Uppercase to Hide: "))
num_string = ""
lower_string = ""

for char in secret_string:
    num_string += str(ord(char) - 23)

print("The Hidden word in Unicode is:", num_string)
secret_string = ""

for i in range(0, len(num_string)-1, 2):
    num_char = str(num_string[i] + num_string[i+1])
    num_char = int(num_char)
    secret_string += str(chr(num_char+23))
#    lower_string += str(chr(num_char) + 55)

print("The Hidden word decoded is:", secret_string)
# print("The Hidden word lowercase is:", lower_string)

# A - Z 65 - 90
# a - z 97 - 122

# print("A = ", ord("A"))
# print("65 = ", chr(65))