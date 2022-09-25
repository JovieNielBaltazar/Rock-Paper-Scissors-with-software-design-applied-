import random


class Rock_Paper_Scissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.round = 1
        self.user = None
        self.player_points = 0
        self.computer_points = 0

    def launch(self):
        
        self.rounds = input("How many rounds do you want the game to have? : ")

        if self.is_number():
            return self.rounds
        else:
            print("invalid Input!")
            return self.launch()

    def get_user_input(self):
        user = str(input("Rock, Paper, Scissors? : ")).lower()

        if user not in self.choices:
            print("Invalid Input!")
            return self.get_user_input()
        else:
            return str(user)

    def scores(self):
        print(f"Player: {self.player_points}")
        print(f"Computer: {self.computer_points}")

    def player_wins(self):
        print("Player wins!")
        self.player_points += 1
        self.scores()

    def computer_wins(self):
        print("Computer wins!")
        self.computer_points += 1
        self.scores()

    def tie(self):
        print("Its a Tie!")
        self.scores()


    def decision(self, user, computer):

        if user == "rock":
            if computer == "scissors":
                self.player_wins()
            elif computer == "paper":
                self.computer_wins()
            else:
                self.tie()

        elif user == "paper":
            if computer == "scissors":
                self.computer_wins()
            elif computer == "rock":
                self.player_wins()
            else:
                self.tie()

        else:
            if computer == "rock":
                self.computer_wins()
            elif computer == "paper":
                self.player_wins()
            else:
                self.tie()

    def is_number(self):
        try:
            rounds_number = int(self.rounds)
        except:
            return False

        return rounds_number

    def game_run(self):

        print("Welcome to rock paper scissors game!")
        self.launch()

        while True:

            computer = random.choice(self.choices)

            if self.round < (int(self.rounds) + 1):

                print(f"Round {self.round}")
                user = self.get_user_input()
                print(f"Computer: {computer}")
                self.decision(user, computer)
                print("\n")
                self.round += 1

            else:
                
                print(f"Total scores, \nPlayer: {self.player_points} \nComputer: {self.computer_points}")

                if self.player_points > self.computer_points:
                    print("Over all winner is Player!")
                elif self.player_points < self.computer_points:
                    print("Over all winner is Computer!")
                else:
                    print("It's a tie!")

                print("Thank you for Playing!")
                break

        
game = Rock_Paper_Scissors()
game.game_run()