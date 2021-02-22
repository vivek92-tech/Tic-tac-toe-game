
from tickTacToe import TicTacToe
import pytest

@pytest.fixture
def ttt_obj():
   ttt_obj = TicTacToe()
   return ttt_obj

def test_place_marker(ttt_obj):
   result1 = ttt_obj.place_marker('x',2,1)
   assert result1 == True
   result2 = ttt_obj.place_marker('o', 2, 1)
   assert result2 == False

def test_game_result_row1(ttt_obj): # test for row-1
   players_dict = {"player-1":"x", "player-2":"o"} 
   ttt_obj.board[0][0] = 'x'
   ttt_obj.board[0][1] = 'x'
   ttt_obj.board[0][2] = 'x'
   result1=ttt_obj.game_result(players_dict)
   assert result1 == True
   ttt_obj.board[0][0] = 'o'
   result2=ttt_obj.game_result(players_dict)
   assert result2 == False

def test_game_result_row2(ttt_obj): # test for row-2
   players_dict = {"player-1":"x", "player-2":"o"} 
   ttt_obj.board[1][0] = 'x'
   ttt_obj.board[1][1] = 'x'
   ttt_obj.board[1][2] = 'x'
   result1=ttt_obj.game_result(players_dict)
   assert result1 == True
   ttt_obj.board[1][0] = 'o'
   result2=ttt_obj.game_result(players_dict)
   assert result2 == False

def test_game_result_row3(ttt_obj): # test for row-3
   players_dict = {"player-1":"x", "player-2":"o"} 
   ttt_obj.board[2][0] = 'x'
   ttt_obj.board[2][1] = 'x'
   ttt_obj.board[2][2] = 'x'
   result1=ttt_obj.game_result(players_dict)
   assert result1 == True
   ttt_obj.board[2][0] = 'o'
   result2=ttt_obj.game_result(players_dict)
   assert result2 == False

def test_game_result_column1(ttt_obj): # test for column-1
   players_dict = {"player-1":"x", "player-2":"o"} 
   ttt_obj.board[0][0] = 'x'
   ttt_obj.board[1][0] = 'x'
   ttt_obj.board[2][0] = 'x'
   result1=ttt_obj.game_result(players_dict)
   assert result1 == True
   ttt_obj.board[2][0] = 'o'
   result2=ttt_obj.game_result(players_dict)
   assert result2 == False

def test_game_result_column2(ttt_obj): # test for column-2
   players_dict = {"player-1":"x", "player-2":"o"} 
   ttt_obj.board[0][1] = 'x'
   ttt_obj.board[1][1] = 'x'
   ttt_obj.board[2][1] = 'x'
   result1=ttt_obj.game_result(players_dict)
   assert result1 == True
   ttt_obj.board[2][1] = 'o'
   result2=ttt_obj.game_result(players_dict)
   assert result2 == False

def test_game_result_column3(ttt_obj): # test for column-3
   players_dict = {"player-1":"x", "player-2":"o"} 
   ttt_obj.board[0][2] = 'x'
   ttt_obj.board[1][2] = 'x'
   ttt_obj.board[2][2] = 'x'
   result1=ttt_obj.game_result(players_dict)
   assert result1 == True
   ttt_obj.board[2][2] = 'o'
   result2=ttt_obj.game_result(players_dict)
   assert result2 == False

def test_game_result_diagonal1(ttt_obj): # test for diagonal-1 
   players_dict = {"player-1":"x", "player-2":"o"} 
   ttt_obj.board[0][0] = 'x'
   ttt_obj.board[1][1] = 'x'
   ttt_obj.board[2][2] = 'x'
   result1=ttt_obj.game_result(players_dict)
   assert result1 == True
   ttt_obj.board[0][0] = 'o'
   result2=ttt_obj.game_result(players_dict)
   assert result2 == False

def test_game_result_diagonal2(ttt_obj): # test for second diagonal
   players_dict = {"player-1":"x", "player-2":"o"} 
   ttt_obj.board[0][2] = 'x'
   ttt_obj.board[1][1] = 'x'
   ttt_obj.board[2][0] = 'x'
   result1=ttt_obj.game_result(players_dict)
   assert result1 == True
   ttt_obj.board[1][1] = 'o'
   result2=ttt_obj.game_result(players_dict)
   assert result2 == False
