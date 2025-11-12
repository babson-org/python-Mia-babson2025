 #Returns True if all non-mine cells are revealed 
def game_won(board, revealed): 
    for r in range(len(board)): 
        for c in range(len(board[0])): 
            # Mines are represented by the number 10, not "M" 
            if board[r][c] != 10 and (r, c) not in revealed: 
                return False 
    return True 