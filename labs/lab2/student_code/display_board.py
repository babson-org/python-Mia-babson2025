#Step 1: Define helper function cell(value) to show selections
#Step 2: Clear the screen
#Step 3: Loop through the 3 rows to print spacing and separators

from utils import clear_screen
def print_board(board: list[int]):
    """
        Display the Tic-Tac-Toe board with human-friendly layout.
        Remember the board may look like:
        [10, 2, 3, 4, -10, 6, 7, 8, 10] after 3 moves and print_board
        
        X | 2 | 3
        ---------
        4 | O | 6
        ---------
        7 | 8 | X
    """
    #Helper Function
    #Shows Player X and O's selections on board
    def cell(value: int) -> str:
        if value == 10: return 'X'  #Player X selection
        elif value == -10: return 'O'  #Player O selection
        else: return str(value) #original cell number
        
    clear_screen()
    
    #Printing the board
    for row in range(3):     #Looping through the rows
        row_values = [cell(board[row * 3 + col]) for col in range(3)]
        print('   |   |   ')  #spacing
        print(f' {row_values[0]} | {row_values[1]} | {row_values[2]} ')
        print('   |   |   ')  #spacing
        if row < 2:
            print('-----------')   #horizontal separator
    print()
