class User:
    def __init__(self, *, username, move_type):
        self.username = username
        self.move_type = move_type

    def move(self, board, cell):
        y = (cell - 1) // 3
        x = (cell - 1) % 3

        if board[y][x] == '.':
            board[y][x] = self.move_type
            return True
        else:
            print('Ячейка не активна!')
            return False