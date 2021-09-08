# Tic-tac-toe-game
Tic tac toe game in python with test cases 

# Features:

This project contains the logic of tic tac toe game along with the following custom methods

* play_tick_tac_toe() - main logical flow of the program
* display_board() - to display the current status of the board
* clear_board() -  to clear the board and put spaces on each place
* place_maker() - to place the player symbol on the board
* winner() - to declare the winner between player-1 and player-2
* game_result() - to check if there is a winner between player-1 and player-2
* select_symbol() - to assign symbol 'x' or 'o' to player-1 and remaining choice symbol to player-2
* select_position() - to select the rows and column in between 1-3 for current player
* play_again() - checks if user wants to play the game again

There are also 9 test cases to test the winner()

# Technology used:

* python3
* pytest

### To run the code

* clone the repository `git clone https://github.com/vivek92-tech/Tic-tac-toe-game.git`
* Install **requirements.txt** file `pip install -r requirements.txt`
* navigate to **/Tic-tac-toe-game-main** folder and run the program with `python tickTacToe.py` command and play the game according to the instructions. 

### To run unit testing
* navigate to **/Tic-tac-toe-game-main/tests** folder and run the tests with `pytest test_tickTacToe.py` command 
 
