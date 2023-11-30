
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

# Function to check if any player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to play the Tic Tac Toe game
def play_game():
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    # Game loop
    while not game_over:
        # Print the board
        print_board(board)

        # Get the current player's move
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Make the move
        if board[row][col] == ' ':
            board[row][col] = current_player

            # Check if the current player wins
            if check_winner(board, current_player):
                print("Player", current_player, "wins!")
                game_over = True
            else:
                # Switch to the other player
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

        # Check if the board is full (tie)
        if all(cell != ' ' for row in board for cell in row) and not game_over:
            print("It's a tie!")
            game_over = True

    # Print the final board
    print_board(board)

# Start the game
play_game()
