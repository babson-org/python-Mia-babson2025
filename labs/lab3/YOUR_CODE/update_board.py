""" update_board.py Handles what happens when the player "clicks" a cell. If the cell has 0 mines around it, the function keeps revealing more nearby cells (this is called "flood fill"). """ 

import globals as g 
from get_adjacent_cells import get_adjacent_cells 

def reveal_cell(board, row, col, revealed): """ Reveals the chosen cell and expands if it’s a 0-cell. 

Args: 
    board: the hidden board with all numbers and mines 
    row, col: coordinates of the cell the player picked 
    revealed: a set that keeps track of which cells are already shown 
""" 
 
    # Stop if this cell has already been revealed 
    if (row, col) in revealed: 
        return 
    
    # Mark the cell as revealed 
    revealed.add((row, col)) 
    
    cell_value = board[row][col] 
    
    # Show the correct symbol on the display board 
    if cell_value == 0: 
        g.display_board[row][col] = g.BLANK  # blank = no mines nearby 
    elif cell_value == 10: 
        g.display_board[row][col] = g.MINE   # show mine (💣) 
    else: 
        g.display_board[row][col] = str(cell_value)  # show number 
    
    # If the cell is empty (0), automatically reveal all neighbors 
    if cell_value == 0: 
        for (nr, nc) in get_adjacent_cells(row, col): 
            if (nr, nc) not in revealed: 
                # Recursive call: reveal the next cell 
                reveal_cell(board, nr, nc, revealed) 
    