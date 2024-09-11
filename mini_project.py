# Project 3: Rock, Paper, Scissors

import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    player_wins = 0
    computer_wins = 0
    while player_wins < 2 and computer_wins < 2:
        player = None
        computer = random.choice(options)

        while player not in options:
            player = input("Enter a choice (rock, paper, scissors): ")

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
            player_wins += 1
        elif player == "paper" and computer == "rock":
            print("You win!")
            player_wins += 1
        elif player == "scissors" and computer == "paper":
            print("You win!")
            player_wins += 1
        else:
            print("You lose!")
            computer_wins += 1
    if player_wins == 2:
        print("You won the best of 3: Thanks for playing!")
    else:
        print("The computer won the best of 3: Thanks for playing!")
    running = False