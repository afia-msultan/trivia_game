'''
This code simulates a generic trivia game where various input files (with questions and answers) can be used to play the game.
For example, if a file with all the countries and their capitals is used as an input file, then the user can play a trivia game
where they would guess the capitals of various countries. The format and content of the question asked by the game will also
dynamically change by depending on the game; this is done using the header in the corresponding input file. As a result, this
code serves as a generic backbone for any type of trivia game provided there is an input file containing the questions and answers;
2 such files are used in this code to simulate 2 unique games.

The game is also equipped with several other features to enhance the user's gaming experience. There is a scoring system
in the game which keeps track of the user's name, time they played the game and the score they achieved. All past games
played by the user are saved and can be viewed at a later time. This allows this game to also be a multiplayer game where
multiple users can compete with one another and determine the winner by viewing each others past scores and keeping track
of their individual scores through their save names and timestamps. Additionally, the code also makes use of python's time
module to set a 15 second timer for each question (the user must answer each question within this timeframe to recieve a
point for the question). This further enhances the game and allows for an added challenge.

'''


# 1 - import modules

import os.path
import glob
from main_menu import main_menu

# 2 - Getting absolute path of the script folder
working_folder = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = "data"


# 3 - the main part of the game doing all of the stuff
if __name__ == '__main__':

    # 4 - getting list of all the game files
    games = glob.glob(os.path.join(working_folder, DATA_FOLDER, "*.csv"))

    while True:
        for index, value in enumerate(games):
            # 5 - displaying list of games as option - using input file title
            print(f"{index+1}. {os.path.basename(value).split('.')[0]}")
        try:
            option = int(input("Enter a valid integer from the following list: "))
        except ValueError:
            print("Incorrect option. Please enter correct option.")
            continue
        if option > len(games):
            print("Incorrect option. Please enter correct option.")
        else:
            print(f"\nStarting game {os.path.basename(games[option - 1]).split('.')[0]}...\n")
            main_menu(games[option-1])
            break
