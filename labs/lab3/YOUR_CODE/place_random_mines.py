''' 

function: place_random_mines 

 

This function randomly adds a "mine" to different sqaures on the board. 

The function will call board in order to place the mine in the cell of the board 

similar to tic - tac - toe, placing a mine will mean putting a certain number 

into the cell.  

''' 

""" 

Randomly place mines on the board. 

     

Args: 

    board (list of lists): 2D board with empty cells (usually 0). 

         

Returns: 

    list of lists: Board with mines placed (marked as 10). 

""" 

 

import random #random is ALREADY BUILT INTO PYTHON  

import globals #this is calling the OG board characters that we need 

 

mine_val = 10  # Value to represent a mine  

 

 

#the board is a 2D list given as an array, again like tictactoe 

def place_random_mines(board): 

 

    mines_placed = 0 

     

    while mines_placed < globals.MINES: 

        #*refers to global 

        #random row 

        row = random.randint(0, globals.ROWS - 1) 

        #random col 

        col = random.randint(0, globals.COLS - 1) 

         

        # Only place mine if the cell is empty 

        if board[row][col] != mine_val: 

            board[row][col] = mine_val

            mines_placed += 1 

     

    return board 

     

 