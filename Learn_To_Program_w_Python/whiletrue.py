import random

rand_num = random.randrange(1,11)

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == rand_num:
        print("You Guessed It!!")
        break
