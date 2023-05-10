import random
options_list = ["paper", "rock", "scissors"]

win = "You win!"
lose = "You lose!"
player_choice = input("paper, rock or scissors? ").lower()

computer_choice = random.choice(options_list)
print("Computer has choosen: " + computer_choice)

if computer_choice == player_choice:
    print("It's a tie!")
if player_choice == "paper" and computer_choice == "rock":
    print(win)
if player_choice == "scissors" and computer_choice == "paper":
    print(win)
if player_choice == "rock" and computer_choice == "scissors":
    print(win)
if player_choice == "rock" and computer_choice == "paper":
    print(lose)
if player_choice == "scissors" and computer_choice == "rock":
    print(lose)
if player_choice == "paper" and computer_choice == "scissors":
    print(lose)
