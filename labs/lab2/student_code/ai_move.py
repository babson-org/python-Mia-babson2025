def ai_move(board: list[int]):
    """
        Simple AI that selects the first available cell.
        Remember board is a list that starts with items 1 - 9
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        after two moves with X choosing 1 and O choosing 5 the board looks like:
        [10, 2, 3, 4, -10, 6, 7, 8, 9]
        
        so in this case your function should return 2
    """
  
    #Step 1: Loop through board
    #Step 2: Find first open index
    #Step 3: Return Index as AI's move
  
    for idx in range(9):
        if abs(board[idx]) != 10: return idx

 
    