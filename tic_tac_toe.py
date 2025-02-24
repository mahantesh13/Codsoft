import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def is_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell == ' ']

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    if is_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0
    if is_maximizing:
        best_score = -float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for m in get_available_moves(board):
        board[m[0]][m[1]] = 'O'
        score = minimax(board, 0, False)
        board[m[0]][m[1]] = ' '
        if score > best_score:
            best_score = score
            move = m
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while not is_board_full(board) and not is_winner(board, 'X') and not is_winner(board, 'O'):
        print_board(board)
        if current_player == 'X':
            move = tuple(map(int, input("Enter your move (row and column): ").split()))
        else:
            move = best_move(board)
            print(f"AI move: {move[0]} {move[1]}")
        if board[move[0]][move[1]] == ' ':
            board[move[0]][move[1]] = current_player
            current_player = 'O' if current_player == 'X' else 'X'
    print_board(board)
    if is_winner(board, 'X'):
        print("You win!")
    elif is_winner(board, 'O'):
        print("AI wins!")
    else:
        print("It's a tie!")

play_game()
