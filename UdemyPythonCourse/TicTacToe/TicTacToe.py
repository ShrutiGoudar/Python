'''
TicTacToe Game Functions
Author: Shruti Goudar
Created: November 2025
License: MIT License

Description: Core game logic functions for a console-based Tic-Tac-Toe game.
             Includes board display, user input validation, and win condition checking.

Board Layout:
      1 |  2  | 3
    ---------------
      4 |  5  | 6
    ---------------      
      7 |  8  | 9

Functions:
    - print_board(): Display current game board
    - read_user_symbol(): Get player symbol selection
    - check_board_state(): Check if board has available moves
    - read_user_cell_position(): Get valid cell selection from player
    - check_game_status(): Check for win/tie conditions
'''

# Game configuration
__version__ = "1.0.0"
__author__ = "Shruti Goudar"

palyer1 = 'X'       # Default symbols
player2 = 'O'
gameBoard = [1,2,3,4,5,6,7,8,9]  # Game board state

def print_board() :  # Display current board
    print("  {} |  {}  |  {}".format(gameBoard[0], gameBoard[1], gameBoard[2]))
    print("-" * 15)
    print("  {} |  {}  |  {}".format(gameBoard[3], gameBoard[4], gameBoard[5]))
    print("-" * 15)
    print("  {} |  {}  |  {}".format(gameBoard[6], gameBoard[7], gameBoard[8]))
    return 0

def print_board_with_index(position, symbol):
    gameBoard[position-1] = symbol
    print_board()
    return 0

def read_user_symbol():  # Get player symbol choice
    valid_symbols = ["X", "O"]
    sym = input("Enter your choice of symbol X or O :\t").strip().upper()
    while True:
        if sym in valid_symbols:
            sym2 = "O" if sym == "X" else "X"
            return [sym, sym2]
        elif sym.upper() == "Q":
            print("Thanks for playing, Bye Bye!!")
            exit()
        sym = input("Invalid Choice re-enter or Q to quit game :\t").strip().upper()
        
def check_board_state():  # return true if board is not yet full
    notFull = int in [type(x) for x in gameBoard]
    return notFull

def read_user_cell_position():  # Get valid cell position from player
    if (not check_board_state()):
            print("Board is full, Game Over!! Bye Bye")
            return 0
    
    cell_inp = input("Enter your choice of cell number for this turn, range : 1 to 9 or Q to exit :\t")
        
    while True: 
        if cell_inp.upper() == 'Q' :
            print("Game Over! Bye Bye")
            exit()    
        
        cell  = int(cell_inp)

        if cell not in range(1, 10):
            cell_inp = input("invalid choice, range : 1 to 9, re-enter or press Q to quit :\t")
        elif gameBoard[cell-1] == 'X' or gameBoard[cell-1]=='O' :
            cell_inp=input("Cell already occupied, pick another")
        else :
            return cell

def check_game_status():  # Check for win/tie conditions
    # Check horizontal wins
    if ((gameBoard[0] == gameBoard[1] == gameBoard[2])
        or (gameBoard[3] == gameBoard[4] == gameBoard[5])
        or (gameBoard[6] == gameBoard[7] == gameBoard[8])):
        return "win"
    
    # Check vertical wins
    if ((gameBoard[0] == gameBoard[3] == gameBoard[6])
        or (gameBoard[1] == gameBoard[4] == gameBoard[7])
        or (gameBoard[2] == gameBoard[5] == gameBoard[8])):
        return "win"

    # Check diagonal wins
    if ((gameBoard[0] == gameBoard[4] == gameBoard[8])
        or (gameBoard[2] == gameBoard[4] == gameBoard[6])):
        return "win"
  
    else:
        return "tie"
    

