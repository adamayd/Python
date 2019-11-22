import sys

file_name = 'recipes.txt'

try:
    my_file = open('recipes.txt', 'x')
    my_file.write('Meatballs\n')
    my_file.close()
except FileExistsError as err:
    print(f"The {file_name} already exists")
except:
    print(f"Unabled to write to the file")
else:
    print(f"Wrote to {file_name}")
finally:
    print(f"Execution completed")
