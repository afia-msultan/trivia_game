import os
from game_logic import game
from load_input import load_game
from rules import rules
from scoring import read_scores


def main_menu(game_file):
    # loading game name through input file title
    title, question_list, answer_list = load_game(game_file)
    game_name = os.path.basename(game_file).split(".")[0]
    print(f'Welcome to the "{game_name}" Game')

    # displaying all options and handling error
    while True:
        print("Enter a valid integer from the following list:")
        print("1. Play game")
        print("2. Display Scores")
        print("3. Display Rules")
        print("4. Quit the game")
        try:
            user_request = int(input('Enter your choice: '))
            print("-" * 20)
        except ValueError:
            print("You have entered incorrect input.")
            continue
        if user_request == 1:
            print("\n")
            game(game_name, title, question_list, answer_list)
        elif user_request == 2:
            scores = read_scores()
            for score in scores:
                print("-" * (len(str(score))))
                print(score)
        elif user_request == 3:
            rules()
        elif user_request == 4:
            print("-"*8)
            print("Goodbye!")
            quit()
        else:
            print("You have entered incorrect input.")
            print("-" * 20)
            continue

