""" get_adjacent_cells.py This file finds all the neighboring cells (around one square) that are still on the game board. Each square can have up to 8 neighbors. """ 

import globals as g 

def get_adjacent_cells(row, col): """ Finds all valid neighbors around a cell. 

Example: The cell in the middle of a 3x3 area 
has 8 neighbors (top, bottom, left, right, and diagonals). 
 
Args: 
    row (int): Row number of the chosen cell 
    col (int): Column number of the chosen cell 
 
Returns: 
    list of (row, col) tuples for every valid neighbor 
""" 
neighbors = [] 
    
    # Check all possible directions around the cell 
    for dr in [-1, 0, 1]:  # dr = "change in row" 
        for dc in [-1, 0, 1]:  # dc = "change in column" 
            # Skip the center cell itself 
            if dr == 0 and dc == 0: 
                continue 
    
            # Calculate the new row and column positions 
            new_row = row + dr 
            new_col = col + dc 
    
            # Only add the neighbor if it's still inside the board 
            if 0 <= new_row < g.ROWS and 0 <= new_col < g.COLS: 
                neighbors.append((new_row, new_col)) 
 
return neighbors 
 