#Step 1: Prompt the user for input
#Step 2: Convert input to integer
#Step 3: Check if selection is in range (1-9) 
#Step 4: Check if selection is not already taken
#Step 5: If move is valid, update the board

def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    
    prompt = "Select an empty cell (1-9): "
    while True:
        try:
            #Convert input to integer
            selection = int(input(prompt))

            #Validate that selection is in range
            if 1 > selection > 9:
                print("Out of range, try again (1-9):")
                continue

            #Validate selection is not taken
            if board[selection - 1] in (10, -10):
                print("Cell taken, try again (1-9):")
                continue

            #Valid selection
            board[selection - 1] = score['player']
            break

            
        except ValueError:
            prompt = "Invalid input. Try again (1-9): "
            
    

