from os import name, system
import random
from time import sleep
choices = ['rock', 'paper' ,'scissior']
print('             CREATED BY PRASH !!')
sleep(1)
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

while True:
    user = input("rock, paper, scissior? : ").lower().strip()
    computer = random.choice(choices)
    
    print("YOU:" , user.upper())
    print("COMPUTER: " , computer.upper())
    if user == computer:
        print('Draw!!')
    elif user == "rock":
        if computer == "paper":
            print('you lose!!')
        else:
            print('you won!!')
    elif user == "paper":
        if computer == "scissior":
            print('you lose!!')
        else:
            print('you won!!')
    elif user == "scissior":
        if computer == "rock":
            print('you lose!!')
        else:
            print('you won!!')
    else:
        print('Use a valid choice!')
    input()
    clear()
    exit = input("play again? (y/n) : ").lower().strip()
    clear()
    if exit == 'n' or exit == "no":
        quit()
