import numpy as np
import random
import copy
import math

class Agent:
    def __init__(self, id, epsilon, lr):
        self.q_values = {}
        self.id = id
        self.epsilon = epsilon
        self.historic = []
        self.lr = lr

    def add_state(self, board, move, init):
        self.historic.append((copy.copy(board), move))
        if repr(board) in self.q_values.keys():
            self.q_values[repr(board)][repr(move)] = init
        else:
            self.q_values[repr(board)] = {repr(move): init}

    def rest_historic(self):
        self.historic = []

    def get_next_move(self, board):
        if random.random() < self.epsilon and repr(board) in self.q_values.keys():
            tmp = max(self.q_values[repr(board)], key=self.q_values[repr(board)].get)
            return np.array([int(tmp[7]), int(tmp[10])], dtype="int64")
        else:
            pos = np.argwhere(board == 0)
            return pos[np.random.randint(len(pos))]

    def update_q_values(self, game_result):
        if game_result == 1:
            q_val = 0.5
            for i, h in enumerate(self.historic[::-1]):
                self.q_values[repr(h[0])][repr(h[1])] += q_val*math.pow(self.lr, i)

        if game_result == self.id*3:
            q_val = 1
            for i, h in enumerate(self.historic[::-1]):
                self.q_values[repr(h[0])][repr(h[1])] += q_val*math.pow(self.lr, i)
        else:
            q_val = 1
            for i, h in enumerate(self.historic[::-1]):
                self.q_values[repr(h[0])][repr(h[1])] -= q_val*math.pow(self.lr, i)
