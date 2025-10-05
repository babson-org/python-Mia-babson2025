#Step 1: Check for a winner
#Step 2: Checking if the board is full 
#Step 3: Game continues if there is no winner

from calc_score import calc_score
def game_over(board: list[int]):
    """
        After every move (see play_game) we check to see if the game 
        is over.  The game is over if calc_score() returns 30 or -30
        or if ther are no open moves left on the board
        Returns True if the game has a winner or no remaining moves, False otherwise.
    """
   
    
    #Checking if someone won
    score = calc_score(board)
    if score == 30 or score == -30:return True #winning combos filled
        
    #Checking if cells are filled
    if all(abs(cell) == 10 for cell in board):return True #all cells filled
        
    #Game is still being played
    return False
    


