import random
from agent import *

resources = ["fish", "grain", "worm", "rat", "cherry"]
feeder = []
deck = {}
end_of_round_goals = []
goals = ["Wingspan < 65\""]
scores = []

def roll_dice(num_dice):
    result = []
    for i in range(0, num_dice):
        result.append(random.choice(resources))
    return result

def reroll_feeder():
    feeder = roll_dice(5)

def initialize_game(num_players):
    #initialize global variables
    global resources
    global feeder
    global scores
    global deck
    global end_of_round_goals
    global goals

    #start empty
    end_of_round_goals = []
    feeder = []
    scores = []

    #initialize scores
    scores = [0]*num_players

    #initialize feeder
    feeder = ["fish", "grain", "worm", "rat", "cherry"]

    #initialize end of round goals
    end_of_round_goals_options = ["Total birds", "Birds in forest", "Birds in grasslands", "Birds in wetlands", "Eggs in stick nest", "Eggs in hole nest", "Eggs in cup nest", "Eggs in pebble nest", "Eggs", "Stick nest with eggs", "Hole nest with eggs", "Cup nest with eggs", "Pebble nest with eggs"]
    for i in range(0,4):
        choice = random.choice(end_of_round_goals_options)
        end_of_round_goals.append(choice)
        end_of_round_goals_options.remove(choice)

def play_game(num_players):
    print("Playing Game")
    print("Scores: " + str(scores))
    for i in range(0, len(end_of_round_goals)): 
        print("End of Round Goal " + str(i+1) + " " + str(end_of_round_goals[i]))

    #4 rounds
    for round in range(1, 5):
        for turn in range(1, 10-round):
            print("Round: " + str(round) + ", Turn: " + str(turn))
            for player in range(1, num_players+1):
                print("Player " + str(player) + " turn")
    exit(1)
    for i in range(0, len(goals)): 
        print("Goal " + str(i+1) + " " + str(goals[i]))
    print("Birdfeeder: " + str(feeder))

