# Allow user to enter string
user_string = str(input("Enter a string: "))

# Clear out extra white space
user_string = user_string.strip()

# Create list of words
words_list = user_string.split()

# Convert String to Acronym
acronym_string = ""
for i in words_list:
    acronym_string += i[0]

# Print Acronym in Uppercase
print(acronym_string.upper())


