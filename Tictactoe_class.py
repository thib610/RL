import numpy as np


class Tictactoe:
    def __init__(self):
        self.board = np.zeros((3, 3))

    def get_board(self):
        return self.board()

    def make_move(self, player, pos):
        self.board[pos[0], pos[1]] = player

    def get_avaliable_pos(self):
        return np.argwhere(self.board == 0)

    def check_end(self):
        for i in range(0, 3):
            res = sum(self.board[i])
            if res == 3 or res == -3:
                return res

        for i in range(0, 3):
            res = sum(self.board[:, i])
            if res == 3 or res == -3:
                return res

        res = self.board[0, 0]+self.board[1, 1]+self.board[2, 2]
        if res == 3 or res == -3:
            return res
        res = self.board[0, 2]+self.board[1, 1]+self.board[2, 0]
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