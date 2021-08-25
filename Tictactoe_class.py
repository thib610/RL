import numpy as np
import random
from parameters import *

# launch game between  2 IA
# p1 and p2: 2 agent
# init: default value for Q_table item
def ia_versus(p1, p2):
    turn = random.randint(0, 1)
    game = Tictactoe()
    check = 0
    while check == 0:
        if turn % 2 == 0:
            next_move = p1.get_next_move(game.board)
            p1.add_state(game.board, next_move)
            game.make_move(-1, next_move)
        else:
            next_move = p2.get_next_move(game.board)
            p2.add_state(game.board, next_move)
            game.make_move(1, next_move)
        check = game.check_end()
        turn += 1
    p1.update_q_values(check)
    p2.update_q_values(check)
    p1.rest_historic()
    p2.rest_historic()
    return game


# launch a game between human and ia
# ia: an agent
def ia_vs_human(ia):
    # turn: variable to choose randomly who start
    turn = random.randint(0, 1)
    game = Tictactoe()
    check = 0  # check have different value depending of the state of the game
    ia.epsilon = 1  # make the ia choose only best move
    print("IA token:",  ia.id)
    if ia.id == -1:
        print("your token:", 1)
    else:
        print("your token:", -1)
    while check == 0:
        if turn % 2 == 0:  # ia turn
            next_move = ia.get_next_move(game.board)
            game.make_move(ia.id, next_move)
        else:  # human turn
            print(game.board)
            valx = input("Enter your x: ")
            valy = input("Enter your y: ")
            game.make_move(1, np.array([int(valx)-1, int(valy)-1]))
        check = game.check_end()
        turn += 1
    print(game.board)  # print last state of the game
    if check == ia.id * 3:
        print("YOU DIED")
    elif check == 1:
        print("equality")
    else:
        print("my ai loose it SUCK")
    return game


class Tictactoe:
    def __init__(self):
        self.board = np.zeros((3, 3))

    def get_board(self):
        return self.board()

    def make_move(self, player, pos):
        self.board[pos[0], pos[1]] = player

    def get_available_pos(self):
        return np.argwhere(self.board == 0)

    # verify if there is a win or a draw
    # return 0 if no end condition
    # -3 when player -1 win
    # 3 when player 1 win
    # 1 in case of draw
    def check_end(self):
        for i in range(0, 3):
            res = sum(self.board[i])
            if res == 3 or res == -3:
                return res

        for i in range(0, 3):
            res = sum(self.board[:, i])
            if res == 3 or res == -3:
                return res

        res = self.board[0, 0] + self.board[1, 1] + self.board[2, 2]
        if res == 3 or res == -3:
            return res
        res = self.board[0, 2] + self.board[1, 1] + self.board[2, 0]
        if res == 3 or res == -3:
            return res
        if len(np.argwhere(self.board == 0)) == 0:
            return 1
        return 0

    def reset_game(self):
        self.board = np.zeros((3, 3))

    def print_board(self):
        print(self.board)

    def get_valid_move(self):
        return np.argwhere(self.board == 0)
