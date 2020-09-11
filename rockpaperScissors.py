from random import *

choice = ["rock","paper","scissors"]

def main():
    computer = choice[randint(0,2)]

    print("Welcome to Rock , Paper ,Scissors ")

    player = input("Your choice: ").lower()

    print("Computers Choice: " + computer)

    if player == computer:
        print("Its a draw")
    elif player == "rock" and computer== "scisssors":
        print("Player wins")
    elif player == "rock" and computer == "paper":
        print("Computer wins")
    elif player == "scissors" and computer == "rock":
        print("Computer wins")
    elif player == "scissors" and computer == "paper":
        print("Player Wins")
    elif player == "paper" and computer == "rock":
        print("Player Wins")
    elif player == "paper" and computer == "scissors":
        print("Computer Wins")

    main()

main()