""" count_adjacent_mines.py Goes through the whole board and counts how many mines are next to each square. Each number on the Minesweeper board shows how many mines are touching that cell. """ 

import globals as g 
from get_adjacent_cells import get_adjacent_cells 

MINE_VALUE = 10 # We'll use 10 to represent a mine 

def count_adjacent_mines(board): """ Updates the board so that each non-mine cell shows how many mines are next to it. 

Args: 
    board: the hidden board that has mine positions (10 = mine) 
""" 
    for r in range(g.ROWS): 
        for c in range(g.COLS): 
    
            # Skip cells that are mines 
            if board[r][c] == MINE_VALUE: 
                continue 
    
            # Count how many of the neighbors are mines 
            mine_count = 0 
            for (nr, nc) in get_adjacent_cells(r, c): 
                if board[nr][nc] == MINE_VALUE: 
                    mine_count += 1 
    
            # Save that number back onto the board 
            board[r][c] = mine_count 
 
return board 
 