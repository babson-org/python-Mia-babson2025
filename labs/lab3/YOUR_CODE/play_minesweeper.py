import globals as g
from initialize_board import initialize_board
from count_adjacent_mines import count_adjacent_mines
from update_board import reveal_cell
from get_validated_input import get_validated_input
from game_won import game_won
from print_board import print_board

def play_minesweeper():
    print("💣 Welcome to Minesweeper!")

    g.board = initialize_board()
    count_adjacent_mines(g.board)

    revealed = set()

    while True: 
        print_board(g.board, 0)
        r, c = get_validated_input(g.ROWS, g.COLS, revealed)

        if g.board[r][c][1] == '💣':
            print("💥Boom! You hit a mine, game over")
            print_board(g.board, 1)
            break

        reveal_cell(g.board, r, c, revealed)

        display_symbol = str(g.board[r][c][1]) if g.board[r][c][1] != " " else " "
        g.board[r][c] = (display_symbol, g.board[r][c][1])

        if game_won(g.board, revealed):
            print_board(g.board, 0)
            print("Congrats! You cleared the board")
            break

if __name__ == "__main__":
    play_minesweeper()