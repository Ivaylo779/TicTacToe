def check_for_winner(table: list, sign) -> None:
    is_row_winner = check_row_winner(table, sign)
    is_col_winner = check_col_winner(table, sign)
    is_diagonal_winner = check_diagonal_winner(table, sign)
    if is_row_winner or is_col_winner or is_diagonal_winner:
        return True
    return False


def check_row_winner(table, sign):
    for curr_row in table:
        if curr_row.count(sign) == 3:
            return True
    return False


def check_col_winner(table, sign):
    for col_idx in range(3):
        count = 0
        for row_idx in range(3):
            if table[row_idx][col_idx] == sign:
                count += 1
        if count == 3:
            return True
    return False


def check_diagonal_winner(table, sign):
    count_primary = 0
    count_secondary = 0
    for index in range(3):
        if table[index][index] == sign:
            count_primary += 1

        if table[index][3 - index - 1] == sign:
            count_secondary += 1

    if count_primary == 3 or count_secondary == 3:
        return True

    return False


def print_board(table: list) -> None:
    for curr_row in table:
        print(f"| {' | '.join(curr_row)} |")


first_player_name = input("Player one name: ")
second_player_name = input("Player two name: ")

first_player_sign = input(f"{first_player_name} would you like to play with 'X' or 'O'? ").upper()
while first_player_sign not in ["X", "O"]:
    print("Please enter either 'X' or 'O'.")
    first_player_sign = input(f"{first_player_name} would you like to play with 'X' or 'O'? ").upper()

second_player_sign = 'X' if first_player_sign == 'O' else 'O'

print("This is the numeration of the board:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")

print(f"{first_player_name} starts first!")

board = [[" ", " ", " "] for _ in range(3)]
mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

turn = 1
while turn < 10:
    current_player = first_player_name if turn % 2 != 0 else second_player_name
    current_sign = first_player_sign if turn % 2 != 0 else second_player_sign

    try:
        position = int(input(f"{current_player} please choose a free position between [1-9]."))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if not (1 <= position <= 9):
        print("Please enter a valid number, between 1 and 9.")
        continue

    row, col = mapper[position]

    if board[row][col] in ['X', 'O']:
        print("This position is already taken.")
        continue

    board[row][col] = current_sign

    print_board(board)

    if turn >= 5 and check_for_winner(board, current_sign):
        print(f"Congratulations! {current_player} wins!")
        break

    turn += 1

else:
    print("It's a draw!\nThanks for playing!")
