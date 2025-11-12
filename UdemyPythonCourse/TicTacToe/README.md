# TicTacToe Game

A console-based Tic-Tac-Toe game implemented in Python.

## Author
**Shruti Goudar**

## Acknowledgments
This project was developed as part of the milestone project from the Udemy Course: **"Complete Python Bootcamp"** by **Jose Portilla**. While the implementation and code are original work, the project concept and helpful guidance came from this excellent course.

## Description
This is a classic Tic-Tac-Toe game where two players take turns placing their symbols (X or O) on a 3x3 grid. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.

## Features
- Interactive console-based gameplay
- Custom player names
- Symbol selection (X or O)
- Input validation and error handling
- Win/tie detection
- Clean, formatted board display

## Files
- `main.py` - Main game controller and entry point
- `TicTacToe.py` - Core game logic and functions
- `README.txt` - Original project hints and guidance from the course
- `README.md` - This documentation file

## How to Play

### Prerequisites
- Python 3.6 or higher

### Installation
1. Clone this repository or download the files
2. Ensure both `main.py` and `TicTacToe.py` are in the same directory

### Running the Game
```bash
python main.py
```

### Game Instructions
1. Enter names for Player 1 and Player 2
2. Player 1 selects their symbol (X or O)
3. Players take turns entering cell numbers (1-9) to place their symbols
4. The game ends when someone gets three in a row or the board is full (tie)

### Board Layout
```
  1 |  2  | 3
---------------
  4 |  5  | 6
---------------      
  7 |  8  | 9
```

## Example Gameplay
```
Enter Player 1 name : Alice
Enter Player 2 name : Bob
Enter your choice of symbol X or O : X
Alice : X
Bob : O

  1 |  2  | 3
---------------
  4 |  5  | 6
---------------
  7 |  8  | 9

Enter your choice of cell number for this turn, range : 1 to 9 or Q to exit : 5
```

## Project Development Notes
This project was developed following the milestone project guidelines from Jose Portilla's Complete Python Bootcamp course. The original project hints and helpful guidance can be found in `README.txt`. The implementation includes:

- Modular code design with separate game logic and main controller
- Comprehensive input validation
- Clear separation of concerns between display, logic, and control
- Error handling for invalid inputs
- Professional code documentation

## Educational Value
This project demonstrates:
- Python function design and organization
- User input handling and validation
- Game state management
- Conditional logic and control flow
- List manipulation and indexing
- String formatting and display

## License
MIT License - feel free to use and modify as needed.

## Course Reference
**Udemy Course:** Complete Python Bootcamp  
**Instructor:** Jose Portilla  
**Project Type:** Milestone Project  

## Contributing
Feel free to fork this project and submit pull requests for improvements!

Note : This file was auto generated