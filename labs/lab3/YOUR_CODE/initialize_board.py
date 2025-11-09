'''

This functions sets up the board that the player will see using our previous written 
functions for our global variables and placing random mines each time the user plays. 
The display board is what shows the diamnds like the traditional game, but the base board 
stays hidden and uses numbers in an array of lists to show where mines will go.  

'''

 

import globals as g 

from place_random_mines import place_random_mines 



def initialize_board(): 

     

    # making empty brds 

    g.base_board = [[0 for _ in range(g.COLS)] for _ in range(g.ROWS)] 

    #ghiddne is the diamonds for the display board  

    g.display_board = [[g.HIDDEN for _ in range(g.COLS)] for _ in range(g.ROWS)] 

 

    #placing minds 

    g.base_board = place_random_mines(g.base_board) 

 

#returns board with placed mines 

    return g.base_board 

 