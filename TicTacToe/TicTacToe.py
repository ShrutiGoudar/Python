'''
      1 |  2  | 3
    ---------------
      4 |  5  | 6
    ---------------      
      7 |  8  | 9

'''

def print_board() :
    return 0


def read_user_symbol():
    valid_symbols = ["X", "O"]
    sym = input("Enter your choice of symbol X or O").strip().upper()
    while True:
        if sym in valid_symbols:
            return sym
        print("Invalid Choice re-enter")
        sym = input().strip().upper()

def read_user_cell_position():
    cell = 0
    return cell



