# Create a list
customers = []

# Create a loop
while True:

    # Get input and make it work for y or n
    createEntry = input("Enter Customer (Yes/No): ")
    createEntry = createEntry[0].lower()

    # Check to leave the loop
    if createEntry == "n":
        break

    # Get customer data
    else:
        fName, lName = input("Enter Customer Name: ").split()

        # Add customer data to list
        customers.append({"fName" : fName, "lName" : lName})

# Print customer data
for cust in customers:
    print(cust["fName"], cust["lName"])

