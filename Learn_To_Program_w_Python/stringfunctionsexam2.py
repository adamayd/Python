msg_to_encrypt = input("Enter to message into Caesar's Cipher: ")
shift_num = int(input("Enter the number to shift: "))
cipher_string = ""

for char in msg_to_encrypt:
    if char.isalpha():
        cipher_num = int(ord(char) + shift_num)
        if char.isupper():
            if cipher_num > 90:
                cipher_num -= 26
            elif cipher_num < 65:
                cipher_num += 26
        else:
            if cipher_num > 122:
                cipher_num -= 26
            elif cipher_num < 97:
                cipher_num += 26
        cipher_string += str(chr(cipher_num))
    else:
        cipher_string += char
print("The Caesars Cipher is: ", cipher_string)

decrypt_string = ""
input("Press Enter to decrypt")
for char in cipher_string:
    if char.isalpha():
        cipher_num = int(ord(char) - shift_num)
        if char.isupper():
            if cipher_num > 90:
                cipher_num -= 26
            elif cipher_num < 65:
                cipher_num += 26
        else:
            if cipher_num > 122:
                cipher_num -= 26
            elif cipher_num < 97:
                cipher_num += 26
        decrypt_string += str(chr(cipher_num))
    else:
        decrypt_string += char
print("Decrypted Message is:", decrypt_string)
