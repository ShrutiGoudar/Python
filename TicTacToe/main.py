"""
TicTacToe Game - Main Controller
Author: Shruti Goudar
Created: November 2025
License: MIT License

Description: Main game controller for console-based Tic-Tac-Toe game.
             Manages player setup, game loop, and determines winners.

Usage: python main.py

Game Flow:
1. Print initial board
2. Take player names and symbol selection
3. Game loop: alternate turns between players
4. Check for win/tie conditions after each move
5. Declare winner or tie
"""

from TicTacToe import *

def main ():
    # Setup: Get player names
    player_names = []
    player_names.append(input("Enter Player 1 name : "))
    player_names.append(input("Enter Player 2 name : "))
    
    # Setup: Display board and assign symbols
    print_board()
    player = read_user_symbol()
    print(f"{player_names[0]} : {player[0]}" )
    print(f"{player_names[1]} : {player[1]}" )
    
    # Game loop
    current_player = 1
    while True:
        # Get player move and update board
        position = read_user_cell_position()
        print_board_with_index(position, player[current_player-1])
        
        # Check game end conditions
        state = check_game_status() 
        if state == "win" :
            print ( f"Congratualtion {player_names[current_player-1]} you Won!! Game over")
            return 0
        elif state == "tie" :
            if not check_board_state():  #true if game continues
                print("Oh O! its a Tie")
                return 0
        
        # Switch turns: 1→2, 2→1
        current_player = 3 - current_player 
    



if __name__ == "__main__":
    main()
