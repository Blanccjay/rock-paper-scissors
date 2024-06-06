# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:38:57 2024

@author: thant
"""

import random

user_wins = 0
com_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    
    if user_input == "q":
        break
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2) #rock = 0, paper = 1, scissors = 2
    
    com_pick = options[random_number]
    print("Computer picked", com_pick + ".")
    
    if user_input == "rock" and com_pick == "scissors":
        print("You won!")
        user_wins += 1
    
    elif user_input == "paper" and com_pick == "rock":
        print("You won!")
        user_wins += 1
    
    elif user_input == "scissors" and com_pick == "paper":
        print("You won!")
        user_wins += 1
    
    else:
        print("YOU LOST")
        com_wins += 1
        
print("You won", user_wins, "times.")
print("The computer won", com_wins, "times.")
print("Have a nice day!")