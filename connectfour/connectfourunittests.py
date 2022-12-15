import unittest
from unittest.mock import patch,call
from connectfourboard import print_board, is_move_valid, place_piece,available_moves, has_won, game_is_over, play_game, is_board_valid

class ConnectFourUnitTests(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.empty_board = [[' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.red_symbol = '\033[2;31;1mR\033[0;0m'
        self.yellow_symbol = '\033[2;33;1mY\033[0;0m'


    def test_is_board_valid_correct_board(self):
        self.assertTrue(is_board_valid(self.empty_board))

    def test_is_board_valid_wrong_board(self):
        board = ""
        self.assertFalse(is_board_valid(board))
    
    @patch('connectfourboard.print')
    def test_print_board_correct_board(self,mocked_print):
        print_board(self.empty_board)
        #call count needs to be 14
        self.assertEqual(mocked_print.call_count,14) 

    @patch('connectfourboard.print')
    def test_print_board_empty_string(self,mocked_print):
        board = ""
        print_board(board)
        self.assertEqual(mocked_print.call_count,1)

    @patch('connectfourboard.print')
    def test_print_board_wrong_board_type(self,mocked_print):
        board = 3
        print_board(board)
        self.assertEqual(mocked_print.call_count,1)
    
    
    #testing is_move_valid
    def test_is_move_valid_correct_board_correct_move(self):
        move = 2
        self.assertTrue(is_move_valid(self.empty_board,move))

    def test_is_move_valid_correct_board_incorrect_move(self):
        move = 10
        self.assertFalse(is_move_valid(self.empty_board,move))
    
    def test_is_move_valid_wrong_board(self):
        board = []
        move = 2
        self.assertFalse(is_move_valid(board,move))

    def test_is_move_valid_invalid_move_type(self):
        move = "a"
        self.assertFalse(is_move_valid(self.empty_board,move))
    
    def test_is_move_valid_invalid_board_type(self):
        board = 2
        move = 3
        self.assertFalse(is_move_valid(board,move))

    #testing available_moves
    def test_available_moves_correct_board_empty(self):
        self.assertEqual(available_moves(self.empty_board),[1, 2, 3, 4, 5, 6, 7])

    def test_available_moves_incorrect_board(self):
        board = ""
        self.assertEqual(available_moves(board),[])

    def test_available_moves_correct_board_full_column(self):
        board = [[self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(available_moves(board),[2, 3, 4, 5, 6, 7])

    def test_available_moves_correct_board_almost_full_first_column(self):
        board = [[' ', self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(available_moves(board),[1, 2, 3, 4, 5, 6, 7])
    
    def test_available_moves_correct_board_almost_full_first_and_last_column(self):
        board = [[' ', self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol]]
        self.assertEqual(available_moves(board),[1, 2, 3, 4, 5, 6, 7])

    #testing has_won
    def test_has_won_first_colum_vertical_win_red(self):
        board = [[' ', ' ', self.red_symbol, self.red_symbol, self.red_symbol, self.red_symbol], 
        [' ', ' ', ' ', self.yellow_symbol, self.yellow_symbol, self.yellow_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertTrue(has_won(board,self.red_symbol))
    
    def test_has_won_second_colum_vertical_win_red(self):
        board = [[' ', ' ', ' ', self.yellow_symbol, self.yellow_symbol, self.yellow_symbol], 
        [' ', ' ', self.red_symbol, self.red_symbol, self.red_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertTrue(has_won(board,self.red_symbol))
    
    def test_has_won_third_colum_vertical_win_red(self):
        board = [[' ', ' ', ' ', self.yellow_symbol, self.yellow_symbol, self.yellow_symbol],  
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', self.red_symbol, self.red_symbol, self.red_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertTrue(has_won(board,self.red_symbol))
    
    def test_has_won_fourth_colum_vertical_win_red(self):
        board = [[' ', ' ', ' ', self.yellow_symbol, self.yellow_symbol, self.yellow_symbol],  
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', self.red_symbol, self.red_symbol, self.red_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertTrue(has_won(board,self.red_symbol))
    
    def test_has_won_fifth_colum_vertical_win_red(self):
        board = [[' ', ' ', ' ', self.yellow_symbol, self.yellow_symbol, self.yellow_symbol],  
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', self.red_symbol, self.red_symbol, self.red_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertTrue(has_won(board,self.red_symbol))

    def test_has_won_sixth_colum_vertical_win_red(self):
        board = [[' ', ' ', ' ', self.yellow_symbol, self.yellow_symbol, self.yellow_symbol],  
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', self.red_symbol, self.red_symbol, self.red_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertTrue(has_won(board,self.red_symbol))
    
    def test_has_won_seventh_colum_vertical_win_red(self):
        board = [[' ', ' ', ' ', self.yellow_symbol, self.yellow_symbol, self.yellow_symbol],  
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', self.red_symbol, self.red_symbol, self.red_symbol, self.red_symbol]]
        self.assertTrue(has_won(board,self.red_symbol))

    def test_has_won_horizontal_win_bottom_row(self):
        board = [[' ', ' ', self.yellow_symbol, self.yellow_symbol, self.yellow_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertTrue(has_won(board,self.red_symbol))

    def test_has_won_horizontal_win_top_row(self):
        board = [[self.red_symbol, ' ', self.yellow_symbol, self.yellow_symbol, self.yellow_symbol, self.red_symbol], 
        [self.red_symbol, ' ', ' ', ' ', ' ', self.red_symbol], 
        [self.red_symbol, ' ', ' ', ' ', ' ', self.red_symbol], 
        [self.red_symbol, ' ', ' ', ' ', ' ', ' '], 
        [self.red_symbol, ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertTrue(has_won(board,self.red_symbol))

    def test_has_won_diagonal_win_yellow_top_left_to_bottom_right(self):
        board = [[' ', ' ', self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol], 
        [' ', ' ', ' ', self.yellow_symbol, self.red_symbol, self.yellow_symbol], 
        [' ', ' ', ' ', self.red_symbol, self.yellow_symbol, self.red_symbol], 
        [' ', ' ', ' ', self.yellow_symbol, self.red_symbol, self.yellow_symbol], 
        [' ', ' ', ' ', self.red_symbol, self.yellow_symbol, self.red_symbol], 
        [' ', ' ', ' ', self.yellow_symbol, self.red_symbol, self.yellow_symbol], 
        [' ', ' ', ' ', self.red_symbol, self.yellow_symbol, self.red_symbol]]
        self.assertTrue(has_won(board,self.yellow_symbol))

    def test_has_won_diagonal_win_yellow_bottom_left_to_top_right(self):
        board = [[' ', ' ', ' ', self.red_symbol, self.yellow_symbol, self.red_symbol], 
        [' ', ' ', ' ', self.yellow_symbol, self.red_symbol, self.yellow_symbol], 
        [' ', ' ', ' ', self.red_symbol, self.yellow_symbol, self.red_symbol], 
        [' ', ' ', ' ', self.yellow_symbol, self.red_symbol, self.yellow_symbol], 
        [' ', ' ', ' ', self.red_symbol, self.yellow_symbol, self.red_symbol], 
        [' ', ' ', ' ', self.yellow_symbol, self.red_symbol, self.yellow_symbol], 
        [' ', ' ', self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol]]
        self.assertTrue(has_won(board,self.yellow_symbol))

    def test_has_won_no_four_symbols_connected(self):
        board = [[' ', ' ', ' ', ' ', self.red_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', self.red_symbol, self.yellow_symbol], 
        [' ', ' ', ' ', ' ', ' ', self.yellow_symbol], 
        [' ', ' ', ' ', ' ', ' ', self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', self.yellow_symbol], 
        [' ', ' ', ' ', ' ', ' ', self.yellow_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertFalse(has_won(board,self.yellow_symbol))

    def test_has_won_wrong_board(self):
        board = ""
        self.assertFalse(has_won(board,self.red_symbol), False)

    def test_has_won_wrong_symbol(self):
        board = [[' ', ' ', 'T', 'T', 'T', 'T'], 
        [' ', ' ', ' ', 'Z', 'Z', 'Z'], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertFalse(has_won(board,self.red_symbol), False)

    #testing place_piece
    def test_place_piece_in_first_column(self):
        column = 1
        player = self.red_symbol
        self.assertTrue(place_piece(self.empty_board,column,player))

    def test_place_piece_in_almost_full_first_column(self):
        board = [[' ', self.red_symbol, self.red_symbol, self.yellow_symbol, self.yellow_symbol, self.yellow_symbol], 
        [' ', ' ', ' ', self.red_symbol, self.yellow_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        column = 1
        player = self.red_symbol
        self.assertTrue(place_piece(board,column,player))

    def test_place_piece_in__full_first_column(self):
        board = [[self.red_symbol, self.red_symbol, self.red_symbol, self.yellow_symbol, self.yellow_symbol, self.yellow_symbol], 
        [' ', ' ', ' ', self.red_symbol, self.yellow_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        column = 1
        player = self.red_symbol
        self.assertFalse(place_piece(board,column,player))

    def test_place_piece_invalid_column(self):
        column = 8
        player = self.red_symbol
        self.assertFalse(place_piece(self.empty_board,column,player))

    def test_place_piece_invalid_board(self):
        board = ""
        column = 2
        player = self.yellow_symbol
        self.assertFalse(place_piece(board,column,player))

    #testing game_is_over
    def test_game_is_over_red_wins(self):
        board = [[' ', ' ', self.red_symbol, self.red_symbol, self.red_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertTrue(game_is_over(board))
    
    def test_game_is_over_yellow_wins(self):
        board = [[' ', ' ', self.yellow_symbol, self.yellow_symbol, self.yellow_symbol, self.yellow_symbol], 
        [' ', ' ', ' ', self.red_symbol, self.red_symbol, self.red_symbol], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertTrue(game_is_over(board))

    def test_game_is_over_tie(self):
        board = [[self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol], 
        [self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol], 
        [self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol], 
        [self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol], 
        [self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol], 
        [self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol], 
        [self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol, self.yellow_symbol, self.red_symbol]]
        self.assertTrue(game_is_over(board))

    #testing play_game

    @patch('connectfourboard.has_won')
    @patch('connectfourboard.input')
    def test_play_game_input_call(self,mocked_input,mocked_has_won):
        mocked_input.return_value = 1
        mocked_has_won.side_effect = [False,False, True]
        calls = [call([[' ', ' ', ' ', ' ', ' ', self.red_symbol], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']], self.red_symbol),
 call([[' ', ' ', ' ', ' ', ' ', self.red_symbol], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']], self.yellow_symbol),
 call([[' ', ' ', ' ', ' ', ' ', self.red_symbol], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']], self.red_symbol)]
        play_game()
        print(mocked_has_won.mock_calls)
        mocked_has_won.assert_has_calls(calls)


    # print board gets called twice with the same parameters, 
    # because it gets first printed with the simulated first turn (red placing a piece in the 1st column)
    # and the 2nd time because we forced game_is_over to return True on the 2nd turn
    # It also prints "It was a tie"
    # since has_won still has not detected that a player has 4 pieces in a row
    @patch('connectfourboard.input')
    @patch('connectfourboard.game_is_over')
    @patch('connectfourboard.print_board')
    def test_play_game_print_board_call(self,mocked_print_board,mocked_game_is_over,mocked_input):
        mocked_input.return_value = 1
        mocked_game_is_over.side_effect = [False, True]
        calls = [call([[' ', ' ', ' ', ' ', ' ', self.red_symbol], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]),
 call([[' ', ' ', ' ', ' ', ' ', self.red_symbol], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']])]
        play_game()
        mocked_print_board.assert_has_calls(calls)


    # mocking the input so the test doesn't want a real user input
    # setting the return value of the mock to something we would expect as a return
    # if 1 piece has been set it would return an array of all columns, since none are full yet
    @patch('connectfourboard.input')
    @patch('connectfourboard.game_is_over')
    @patch('connectfourboard.available_moves')
    def test_play_game_available_moves_call(self,mocked_available_moves,mocked_game_is_over,mocked_input):
        mocked_available_moves.return_value = [1,2,3,4,5,6,7]
        mocked_input.return_value = 1
        mocked_game_is_over.side_effect = [False,True]
        calls = [call([[' ', ' ', ' ', ' ', ' ', self.red_symbol], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']])]
        play_game()
        mocked_available_moves.assert_has_calls(calls)


    # Setting up the game_is_over function with a MagicMock to return False after the first piece is placed (1 Turn elapsed), 
    # return False after the 2nd piece is placed (2 Turn elapsed)
    #  and then return True (a 3rd piece isn't placed this time)
    # by creating call objects with the expected parameters and then checking if the mock has any calls that match our created ones,
    # we can verify that our function gets called with the right parameters
    @patch('connectfourboard.game_is_over')
    @patch('connectfourboard.input')
    @patch('connectfourboard.place_piece')
    def test_play_game_place_piece_call(self,mocked_place_piece,mocked_input,mocked_game_is_over):
        mocked_game_is_over.side_effect = [False,False,True]
        mocked_input.return_value = 1
        calls = [call([[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']], 1, self.red_symbol),
 call([[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']], 1, self.yellow_symbol)]
        play_game()
        print(mocked_place_piece.mock_calls)
        mocked_place_piece.assert_has_calls(calls)
        
    
    # Setting up the game_is_over function with a MagicMock to return False after the first piece is placed (1 Turn elapsed), 
    # return False after the 2nd piece is placed (2 Turn elapsed)
    #  and then return True (a 3rd piece isn't placed this time)
    @patch('connectfourboard.game_is_over')
    @patch('connectfourboard.input')
    @patch('connectfourboard.is_move_valid')
    def test_play_game_is_move_valid_call(self,mocked_is_move_valid,mocked_input,mocked_game_is_over):
        mocked_game_is_over.side_effect = [False,True]
        mocked_input.return_value = 7
        mocked_is_move_valid.return_value = True
        calls = [call([[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', self.red_symbol]], 1),
 call([[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', self.red_symbol]], 2),
 call([[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', self.red_symbol]], 3),
 call([[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', self.red_symbol]], 4),
 call([[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', self.red_symbol]], 5),
 call([[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', self.red_symbol]], 6),
 call([[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', self.red_symbol]], 7),
 call([[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', self.red_symbol]], 7),
 call([[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', self.red_symbol]], 7)]
        play_game()
        mocked_is_move_valid.assert_has_calls(calls)
        
    

if __name__ == "__main__":
    unittest.main()