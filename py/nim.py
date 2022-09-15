# nim.py
# Steve Sabaugh
# CSCI 77800 Fall 2022
# collaborators: Mike Randazzo (That is the only person I could remember collaborating with on Java NIM during the summer.)
# consulted: 

import random

stones = 12
com_num = random.randint(1, min(3, stones))
print("Lets Play the Game of Nim")
print(f'There are {stones} stones left')

while stones >= 0:

    user_num = int(input("Pick a number from 1 to 3: "))

    stones -= user_num
    print("You removed " + str(user_num) + " stones.")
    print(f'There are {stones} stones left')

    if stones == 0:
        print("You Won!!")
        break

    if stones <= 3:
        com_num = stones

    stones -= com_num

    print("The computer removed " + str(com_num) + " stones")
    print(f'There are {stones} stones left')

    if stones == 0:
        print("The Computer Won!!")
        break

    com_num = random.randint(1, min(3, stones))
    print()
