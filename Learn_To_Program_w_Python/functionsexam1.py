# Solve for x
# x + 4 = 9

# x will always be the 1st value recieved and you only
# will deal with addition

# Receive the string and split the string into variables
def solve_eq(equation):
    x, oper, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    if oper == "+":
        return "x = " + str(num2 - num1)
    elif oper =="-":
        return "x = " + str(num2 + num1)
    elif oper == "*":
        return "x = " + str(num2 / num1)
    else:
        return "x= " + str(num2 * num1)


eq_string = input("Enter an equation (ex. x + 4 = 9): ")
print(solve_eq(eq_string))
