import globals as g 
from initialize_board import initialize_board 
from count_adjacent_mines import count_adjacent_mines 
from update_board import reveal_cell 
from get_validated_input import get_validated_input 
from game_won import game_won 
from print_board import print_board 

def play_minesweeper(): 
    print("💣 Welcome to Minesweeper!") 

    # Create the hidden mine layout 

    g.board = initialize_board() 

    count_adjacent_mines(g.board) 

    revealed = set() 

    while True: 
        print_board(g.display_board, 0) 
        r, c = get_validated_input(g.ROWS, g.COLS, revealed) 

        # A mine is represented by the number 10 (from count_adjacent_mines) 

        if g.board[r][c] == 10: 
            print("BOOOOOM! You hit a mine, game over") 
            print_board(g.display_board, 1) 
            break 

 

        # Reveal the selected cell 
        reveal_cell(g.board, r, c, revealed) 

 

        # Optional: handle display symbol (not tuple-based anymore) 
        display_symbol = " " if g.board[r][c] == 0 else str(g.board[r][c]) 
        g.display_board[r][c] = display_symbol 

 

        if game_won(g.board, revealed): 
            print_board(g.display_board, 0) 
            print("YOU CLEARED THE BOARD!") 
            break 


if __name__ == "__main__": 
    play_minesweeper() 

 