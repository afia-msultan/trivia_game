import random
import time
from scoring import write_scores


def get_options(question, all_incorrect_answers):
    # 13 - randomly selecting option from incorrect answers and adding correct answer to list
    options = random.sample(all_incorrect_answers, 3)
    options.append(question)
    # 14 - shuffling all options
    random.shuffle(options)
    return options


def game(game_name, title, question_list, answer_list):
    user_name = str(input("Enter your name: "))
    score = 0
    questions = 1
    question_duration = 15

    while questions < 10:

        # 15 - keeping track of time for each question
        start_time = time.time()
        end_time = start_time + question_duration

        # 16 - randomly choosing a question
        chosen_question = random.choice(question_list[1:])
        correct_answer = answer_list[question_list.index(chosen_question)]

        # 17 - making list without correct option to choose other options to display
        all_incorrect_answers = list(set(answer_list) - {correct_answer})
        options = get_options(correct_answer, all_incorrect_answers)

        while True:

            print("-" * (24 + len(chosen_question)))
            print("Remaining time:", round((end_time - time.time()), 1), "seconds.")

            print("-" * (24 + len(chosen_question)))
            print(f'What is the {title[1]} of {chosen_question}?')
            print("-"*(24 + len(chosen_question)))
            print("Options:")

            # 18 - using loop to display option along with number
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")

            user_input = input("Enter 1, 2, 3, or 4: ")


            if user_input not in ('1', '2', '3', '4'):
                # 19 - validating user input option
                print("-" * 42)
                print("Invalid input.")
                print("-"*42)
                print('\n')
                continue

            user_input_num = int(user_input) - 1
            if options[user_input_num] == correct_answer and (end_time >= time.time()):
                # 19 - score goes up only if answer is answered correctly and in time
                print("-"*22)
                print("Correct!")
                print("-"*22)
                print('\n')
                score += 10
                break

            elif options[user_input_num] == correct_answer and (end_time < time.time()):
                # 20 - score does not increase if answered in longer than 15 seconds
                print("-" * 69)
                print("Your answer is correct but you took longer than 15 seconds to answer.")
                print("-" * 69)
                print('\n')
                break

            else:
                print("-" * (21 + len(correct_answer)))
                print("Incorrect answer.")
                print("The correct answer is", correct_answer)
                print("-" * (21 + len(correct_answer)))
                print('\n')
                break

        questions += 1


    # 21 - saving game result into dictionary
    current_user_info = {user_name: score}

    # 22 - writing game result to output file
    write_scores(current_user_info, game_name)

    # 23 - displaying result
    print("-"*((len(user_name) + 23 + (len(str(score))))))
    print("Game over!")
    print(f"{user_name}, your final score is {score}")
    print("-" * ((len(user_name) + 23 + (len(str(score))))))

