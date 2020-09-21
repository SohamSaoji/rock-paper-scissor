# code to make tic tac toe in python 
import random
from random import randint
import os 
import time

while True:
    print('press:- ')
    print('1 for rock')
    print('2 for paper')
    print('3 for scissor')
    user_input = int(input("Enter your Choice: "))
    computer_choice = random.randint(1,3)

    while user_input > 3 or user_input < 1:
        user_again = int(input("please enter choice from 1 to 3 only: "))
        user_input = user_again

    if user_input == 1:
        user = 'rock'
    if user_input == 2:
        user == 'paper'
    if user_input == 3:
        user = 'scissor'   

    if computer_choice == 1:
        comp_choice_name = 'rock'
    if computer_choice == 2:
        comp_choice_name == 'paper'
    if computer_choice == 3:
        comp_choice_name = 'scissor'           

    print("                ")
    print(f'user: {user}')
    print(f'computer: {comp_choice_name}')
    print("                  ")

    if user_input == 1 and computer_choice == 3:
        print("user won!!")
        time.sleep(1)
        os.system('cls') # note - os.system('cls') will only work when you run this codde on terminal
    elif user_input == 2 and computer_choice == 1:
        print("user won!!")
        time.sleep(1)
        os.system('cls')    
    elif user_input == 3 and computer_choice == 2:
        print("user won!!")
        time.sleep(1)
        os.system('cls')
    elif user_input == computer_choice:
        print("tie") 
        time.sleep(1)
        os.system('cls')
    else:
        print("computer won!!")
        time.sleep(1)
        os.system('cls')                 

  