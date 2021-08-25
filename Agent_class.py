import numpy as np
import random
import copy
import math
from parameters import *

class Agent:
    def __init__(self, id):
        self.q_values = {}
        self.id = id
        self.epsilon = epsilon_greed
        self.historic = []
        self.lr = lr

    # add a state and a move in historic and in qtable
    def add_state(self, board, move):
        self.historic.append((copy.copy(board), move))
        if repr(board) in self.q_values.keys():
            self.q_values[repr(board)][repr(move)] = init
        else:
            self.q_values[repr(board)] = {repr(move): init}

    def rest_historic(self):
        self.historic = []

    def get_next_move(self, board):
        # if the state isn't in the qtable we update the qtable
        if random.random() < self.epsilon and repr(board) in self.q_values.keys():
            # get the move with the max score for a given state
            tmp = max(self.q_values[repr(board)], key=self.q_values[repr(board)].get)
            # 7 and 10 are the index of x and y in the string representation
            return np.array([int(tmp[7]), int(tmp[10])], dtype="int64")
        else:
            pos = np.argwhere(board == 0)
            return pos[np.random.randint(len(pos))]

    def update_q_values(self, game_result):
        if game_result == 1:
            # update qvalue for the state present in this particular game
            for i, h in enumerate(self.historic[::-1]):
                self.q_values[repr(h[0])][repr(h[1])] += reward_draw*math.pow(self.lr, i)

        if game_result == self.id*3:
            q_val = 1  # reward for win
            for i, h in enumerate(self.historic[::-1]):
                self.q_values[repr(h[0])][repr(h[1])] += reward_win*math.pow(self.lr, i)
        else:
            q_val = 1  # reward for loose
            for i, h in enumerate(self.historic[::-1]):
                self.q_values[repr(h[0])][repr(h[1])] -= abs(reward_loose)*math.pow(self.lr, i)
