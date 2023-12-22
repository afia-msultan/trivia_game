import os.path
from datetime import datetime

# 6 - Getting absolute path of the script folder
# 7 - This will allow program to run from any location
working_folder = os.path.dirname(os.path.abspath(__file__))
score_file = "data/cps109_a1_output.txt"

# 8 - making path of output file by joining working folder path and score file path
scoring_file_path = os.path.join(working_folder, score_file)


def write_scores(name_and_scores, game_name):
    # 9 - opening and appending to output file
    with open(scoring_file_path, 'a') as file:
        # 10 - formatting output for name, game name, timestamp, score
        for key, value in name_and_scores.items():
            current_time = datetime.now()
            datetime_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{key}: {value} | {game_name} | {datetime_str}\n")


def read_scores():
    # 11 - reading the score from output file
    try:
        with open(scoring_file_path, 'r') as file:
            saved_user_info = file.readlines()
    # 12 - handling error if file does not exist
    except FileNotFoundError:
        saved_user_info = ""
    return saved_user_info

