def print_board(board):
    """
    This function prints out the current state of the board.
    """
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('--+---+--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--+---+--')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def get_move(player, board):
    """
    This function prompts the player for their move and returns it.
    """
    valid_move = False
    while not valid_move:
        move = input(f'Player {player}, enter your move (1-9): ')
        try:
            move = int(move) - 1
            if move >= 0 and move <= 8 and board[move] == ' ':
                valid_move = True
            else:
                print('Invalid move. Try again.')
        except ValueError:
            print('Invalid input. Try again.')
    return move

def check_win(board):
    """
    This function checks if either player has won and returns the winning player or None.
    """
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != ' ':
            return board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return board[2]

    # Check for tie
    if ' ' not in board:
        return 'Tie'

    # No winner yet
    return None

def play_game():
    """
    This function plays a game of Tic Tac Toe.
    """
    board = [' '] * 9
    player = 'X'

    while True:
        print_board(board)
        move = get_move(player, board)
        board[move] = player
        winner = check_win(board)
        if winner:
            print_board(board)
            if winner == 'Tie':
                print('Tie game!')
            else:
                print(f'Player {winner} wins!')
            return
        player = 'O' if player == 'X' else 'X'

if __name__ == '__main__':
    play_game()
