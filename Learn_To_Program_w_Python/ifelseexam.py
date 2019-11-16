age = eval(input("Enter Age: "))
if age == 5:
    print("You are in kindergarten")
elif (age >= 6) and (age <=17):
    print("Your are in grade ",age - 5)
elif not (age < 17):
    print("You are in college")
else:
    print("Too young for school")