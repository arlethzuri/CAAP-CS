# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard
moves = 0
name = ''
leaderboard = Leaderboard() #leaderboard object

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
    global name
    global moves
    score = Score(name, moves)
    if won:
        print("\nAt last you made it home! You brush your teeth, shower, then finally lie in bed and fall fast asleep.")
        print("\nGame Over. Congrats, " + name + ", you won! It took you", moves ,"moves.")
        leaderboard.update(score)
    else:
        print ("\nGame Over. Sorry, " + name + ", maybe try again yeah?")
    print("\n")
    name = ''
    moves = 0
    leaderboard.print_board()

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
    while True:
        global name
        global moves 
        print ("Welcome to CTA Adventure! To quit enter ':q' at any time. You will have three lives. Good luck!")
        name = input("\nEnter your name. > ")
        if (name == ':q'):
            exit(1)
        a_map = Map('difficulty')#create a map object, starting at scene to select difficulty
        a_game = Engine(a_map)#pass the map into the engine
        moves = a_game.play()#begin play and return the number of moves into moves variable
        game_over(a_game.won())#pass 

play_game()