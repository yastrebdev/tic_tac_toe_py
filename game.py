def check_cell(cell):
    if cell != '.':
        return cell
    else:
        return False


def check_win(game_board):
    for i, row in enumerate(game_board):
        if row[0] == row[1] and row[1] == row[2]:
            return check_cell(row[0])
        elif game_board[0][i] == game_board[1][i] and game_board[1][i] == game_board[2][i]:
            return check_cell(game_board[0][i])
        elif game_board[0][0] == game_board[1][1] and game_board[1][1] == game_board[2][2]:
            return check_cell(game_board[0][0])
        elif game_board[0][2] == game_board[1][1] and game_board[1][1] == game_board[2][0]:
            return check_cell(game_board[0][2])
        else:
            return  False




def start_game(players, game_board):
    winner = False
    i = 0
    while not winner:
        try:
            cell = int(input('Введите номер ячейки для хода (1-9): '))
        except ValueError:
            print('Введите корректное число.')
            continue

        if cell > 9 or cell < 1:
            print('Введите число от 1 до 9 включительно')
            continue

        is_move = players[i % 2].move(game_board, cell)
        winner = check_win(game_board)

        if is_move:
            i += 1

        if i == 9:
            break

    if winner:
        return f'Выйграл {winner}!'
    else:
        return 'Ничья!'