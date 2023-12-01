#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
# write 'hello world' to the console
# print("hello world")

# create a videogame paper, rock and scissors game
'''
import random
print("Welcome to the Paper, Rock, Scissors game!")
print("Please choose one of the following:")
print("Paper")
print("Rock")
print("Scissors")
player_choice = input()
computer_choice = random.choice(["Paper", "Rock", "Scissors"])
print("Computer chose: " + computer_choice)
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "Paper":
    if computer_choice == "Rock":
        print("You win!")
    else:
        print("You lose!")
elif player_choice == "Rock":
    if computer_choice == "Scissors":
        print("You win!")
    else:
        print("You lose!")
elif player_choice == "Scissors":
    if computer_choice == "Paper":
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid input! You have not entered paper, rock or scissors, try again.")

'''
# create a paper, rock, scissors video game where the player decides whether to play again
import random

while True:
    print("Welcome to the Paper, Rock, Scissors game!")
    print("Please choose one of the following:")
    print("Paper")
    print("Rock")
    print("Scissors")
    player_choice = input()
    computer_choice = random.choice(["Paper", "Rock", "Scissors"])
    print("Computer chose: " + computer_choice)
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            print("You win!")
        else:
            print("You lose!")
    elif player_choice == "Rock":
        if computer_choice == "Scissors":
            print("You win!")
        else:
            print("You lose!")
    elif player_choice == "Scissors":
        if computer_choice == "Paper":
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Invalid input! You have not entered paper, rock or scissors, try again.")
    print("Do you want to play again? (yes/no)")
    if input() != "yes":
        break
print("Thanks for playing!")