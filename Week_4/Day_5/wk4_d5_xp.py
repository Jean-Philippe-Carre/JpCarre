def display_board(board):

    print("*************")
    print("* {} | {} | {} *".format(board[0], board[1], board[2]))
    print("*---|---|---*")
    print("* {} | {} | {} *".format(board[3], board[4], board[5]))
    print("*---|---|---*")
    print("* {} | {} | {} *".format(board[6], board[7], board[8]))
    print("*************")
    print("\n")


def player_input(player):

    while True:
        user_input = input(
            f"{player.title()}, enter your move (1-9) or 'quit' to quit: ").strip().lower()
        print("\n")
        if user_input == 'quit':
            return None
        try:
            position = int(user_input)
            if position < 1 or position > 9:
                print("Invalid position! Please enter a number between 1 and 9.")
            else:
                return position - 1
        except ValueError:
            print("Invalid input! Please enter a number or 'q' to quit.")


def check_win(board, player):

    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def play():
    print("\n")
    player1_name = input("Player 1(X), enter your name: ")
    player2_name = input("Player 2(O), enter the name: ")
    print("\n")
    players = {'X': player1_name, 'O': player2_name}

    board = [' ' for _ in range(9)]
    current_player_symbol = 'X'

    for turn in range(9):
        display_board(board)

        position = player_input(players[current_player_symbol])

        if position is None:
            print(f"{players[current_player_symbol]
                     } has chosen to quit the game. Exiting...")
            return

        while board[position] != ' ':
            print("Position already taken! Choose another position.")
            position = player_input(players[current_player_symbol])
            if position is None:
                print(f"{players[current_player_symbol]
                         } has chosen to quit the game. Exiting...")
                return

        board[position] = current_player_symbol

        if check_win(board, current_player_symbol):
            display_board(board)
            print(f"{players[current_player_symbol].title()} ({
                  current_player_symbol}) wins!")
            print("\n")
            return

        current_player_symbol = 'O' if current_player_symbol == 'X' else 'X'

    display_board(board)
    print("It's a tie!")


play()
