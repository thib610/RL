import numpy as np
import random
import Tictactoe_class
class Agent:
    def __init__(self, id, epsilon):
        self.q_values = {}
        self.id = id
        self.epsilon = epsilon

    def add_q_value(self, board, move, eval):
        if repr(board) in self.q_values.keys():
            self.q_values[repr(board)][repr(move)] = eval
        else:
            self.q_values[repr(board)] = {repr(move): eval}

    def get_next_move(self, board):
        if random.random() < self.epsilon and repr(board) in self.q_values.keys():
            tmp = max(self.q_values[repr(board)], key=self.q_values[repr(board)].get)
            return np.array([int(tmp[7]), int(tmp[10])], dtype="int64")
        else:
            pos = np.argwhere(board == 0)
            return pos[np.random.randint(len(pos))]



