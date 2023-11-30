def evaluate(board):
    # Check rows
    for row in board:
        if all(cell == 'X' for cell in row):
            return 1
        elif all(cell == 'O' for cell in row):
            return -1

    # Check columns
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 1
        elif all(board[row][col] == 'O' for row in range(3)):
            return -1

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(3)):
        return 1
    elif all(board[i][2 - i] == 'X' for i in range(3)):
        return 1
    elif all(board[i][i] == 'O' for i in range(3)):
        return -1
    elif all(board[i][2 - i] == 'O' for i in range(3)):
        return -1

    # No winner, game still ongoing
    return 0

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, maximizing_player):
    score = evaluate(board)

    if score == 1:
        return score - depth
    elif score == -1:
        return score + depth
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

if __name__ == "__main__":
    # Example Tic-Tac-Toe board
    initial_board = [['X', ' ', 'O'],
                     ['O', 'X', ' '],
                     [' ', ' ', 'X']]

    print("Initial Board:")
    print_board(initial_board)

    best_move = find_best_move(initial_board)

    print("Best Move for 'X':", best_move)



