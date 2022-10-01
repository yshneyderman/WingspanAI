import random
from game_utils import *

####
#Written by Yefim Shneyderman
####

print("Welcome to the WingSpan AI: RavenAI")
print("This version makes use of adjusted ruleset by 113Oak")

iterations = 1
num_players = 2

for i in range(0,iterations):
    initialize_game(num_players)
    play_game(num_players)
