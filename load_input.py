import csv

# reading input file
def load_game(input_file):
    questions = []
    answers = []

    with open(input_file, 'r') as csvfile:
        file = csv.reader(csvfile)

        # taking first line as header
        header = next(file)

        # appending rest of the file into either a questions or answers list
        for row in file:
            questions.append(row[0])
            answers.append(row[1])

    return header, questions, answers



