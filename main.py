from User import User
from game import start_game

board = [['.', '.', '.'] for _ in range(3)]

user_x = User(username='Bob', move_type='X')
user_o = User(username='Jon', move_type='O')

match_players = [user_x, user_o]

winner = start_game(match_players, board)

print(winner)