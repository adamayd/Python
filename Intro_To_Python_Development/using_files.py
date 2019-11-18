with = open('cars.txt', 'w+') as my_file:
    my_file.write('Chevelle\n')
    my_file.write('Camaro\n')
    my_file.writelines([
        'Nova\n',
        'Corvette\n',
        'Skylark\n',
    ])

my_file = open('cars.txt', 'r')
with my_file:
    print(my_file.read())
    print("I'm reading again")
    print(my_file.read())
