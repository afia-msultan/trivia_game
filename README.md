# trivia_game
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
