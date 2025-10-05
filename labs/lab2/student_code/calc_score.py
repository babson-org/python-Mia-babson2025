#Step 1:Define Helper Function line_sum(a, b, c) to calculate score
#Step 2: List the 8 winning combinations
#Step 3: Loop through the winning combinations
#Step 4: Find a winner or continue game if no winner

def calc_score(board: list[int]):
    """
        Determines if there's a winner on the board.
        Returns 30 if X wins, -30 if O wins, 0 otherwise.
         
        there are 8 ways to win: 3 rows, 3 columns, 2 diagnols
        if the cells in a row, column or diagnol add up to 30 return 30
        if they add upto -30 return -30
        else return 0
    """
    #Helper Function
    def line_sum(a, b, c):
        '''
            line_sum takes 3 numbers and if the sum is either 30
            or -30 returns that sum otherwise do not return
        '''         
         
        #Sum of rows/columns/diagonal
        if board[a] + board[b] + board[c] == 30:  
            return 30    #Player X is winner
        elif board[a] + board[b] + board[c] == -30:  
            return -30   #Player O is winner
        else:
            return 0     #No winner
   
    #8 Ways to win (Rows/Columns/Diagonals)
    winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4,7), (2, 5, 8), (0,4,8), (2, 4, 6)]

    #Checking cells in each possible winning combo
    for a, b, c in winning_combos:
        result = line_sum(a, b, c)
        if result != 0:    #there is a winner 
            return result
        
    return 0   #there is no winner yet, game still going
    
    
       

