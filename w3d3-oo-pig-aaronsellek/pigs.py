import random
# create computer class
# create computer
# make it so computer rolls die returning number 1-6
# continue rolling unless 1 is rolled or player chooses to "hold"
# if one is rolled no points are awarded
# hold unless it gets 20 points or more
# randomize if the computer will hold or roll
# trying to get total of 100 points

# create human class
# create human interaction
# explain rules of game
# roll die
# after every roll give person chance to roll again or hold
# if one is rolled players turn ends and gets no points
# if player "holds" sum all points from die rollen that round and award to player
# if player gets to 100 they win

# create game class
# greet player
# explain rules
# roll dice to decide who goes first
# state points per player
# after player rolls/holds say points
# other player rolls, sum points if hold
# keep switching until points >= 100
# state player who wins by whoever gets to 100 first
# ask player play again? if "y or yes" yes
# if no end program
# repeat = True

class Game():
    def __init__(self, total_points, computer_score):
        self.total_points = total_points
        self.computer_score = computer_score
    
    def roll_die(self, repeat, hold_points, round_points, player_score):
        print("you rolled " + random.randint(1,6))
        input("roll again? yes, or hold? ")
        round_points == 0
        hold_points = sum(round_points)
        repeat = ("yes" or "y") in input().lower()
        if random.randint ==1
            return print(player_score) and round_points == 0
        else: 
            input("hold ")
            return round_points.append[int] + player_score
class Game():
    def __init__(self, total_points, computer_score):
        self.total_points = total_points
        self.computer_score = computer_score

    def roll_die(self, repeat, hold_points, round_points, player_score):
        print("You rolled ", random.randint(1,6))
        input("Roll again? Yes, or hold? ")
        round_points == 0
        hold_points = sum(round_points)
        repeat = ("yes" or "y") in input().lower()
        if random.randint ==1: 
            return print(player_score) and round_points == 0
        else:
            input("hold ")
            return round_points.append[int] + player_score 
           
    
    def player_score(self, computer_score, player_score, round_points):
        player_score == 0
        computer_score == 0
        player_score + round_points = total_points
        if player_score or computer_score >= 100:
             return input("The game is over, ") #whoever is over 100 wins)

        
    def choose_to_hold_or_roll(self, total_points, hold_points):
        if total_points <= 20:
            choice = random.choice(self.roll_die)
        if total_points >= 20:
            choice = random.choice(hold_points) or random.choice(self.roll_die)
        return choice

def continue_play ():
    play_again = input ("Care to try again? (y/n or yes/no)").lower()
    if play_again.isalpha() and play_again == "y" or play_again == "yes":
        print ("Alright, dont lose to the computer, that would be embarrassing!")
        return True
    if play_again.isalpha() and play_again == "n" or play_again == "no":
        print ("Coward.")
        return False 