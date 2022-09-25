import random

choices = ["rock", "paper", "scissors"]

print("Welcome to rock paper scissors game!")
rounds = int(input("How many rounds do you want the game to have? : "))
round = 1
user = None
player_points = 0
computer_points = 0

def get_user_input():
    user = str(input("Rock, Paper, Scissors? : ")).lower()

    if user not in choices:
        print("Invalid Input!")
        return get_user_input()
    else:
        return str(user)

def player_wins():
    print("Player wins!")
    player_points + 1

def computer_wins():
    print("Computer wins!")
    computer_points + 1

def tie():
    print("Its a Tie!")


def decision(user, computer):

    if user == "rock":
        if computer == "scissors":
            player_wins()
        elif computer == "paper":
            computer_wins()
        else:
            tie()

    elif user == "paper":
        if computer == "scissors":
            computer_wins()
        elif computer == "rock":
            player_wins()
        else:
            tie()

    else:
        if computer == "rock":
            computer_wins()
        elif computer == "paper":
            player_wins()
        else:
            tie()

while True:

    computer = random.choice(choices)

    if round < (rounds+1):

        print(f"round {round}")
        user = get_user_input()
        print(f"Computer: {computer}")
        decision(user, computer)
        round += 1

    else:
        
        print(f"Total scores, \nPlayer: {player_points} \nComputer: {computer_points}")

        if player_points > computer_points:
            print("Over all winner is Player!")
        else:
            print("Over all winner is Computer!")

        print("thank you for Playing!")
        break

    