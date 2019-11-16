adamDict = {"fName": "Adam", "lName": "Ayd",
            "address": "123 Main St"}

print("My Name :", adamDict["fName"])

adamDict["address"] = "215 North St"

print(adamDict)

adamDict["city"] = "Baltimore"

print("Is there a city :", "city" in adamDict)

print(adamDict.values())

print(adamDict.keys())

for k, v in adamDict.items():
    print(k, v)

print(adamDict.get("mName", "Not Here"))

print(adamDict.get("lName", "Not Here"))

del adamDict["fName"]

for i in adamDict:
    print(i)

adamDict.clear()

print(adamDict)

employees = []

fName, lName = input("Enter Employee Name: ").split()

employees.append({"fName" : fName, "lName" : lName})

print(employees)