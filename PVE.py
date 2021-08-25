import Tictactoe_class
import pickle
import random
import agent
import numpy as np

def play(ia):
    turn = random.randint(0, 1)
    game = Tictactoe_class.Tictactoe()
    check = 0
    ia.epsilon = 1
    while check == 0:
        if turn % 2 == 0:
            next_move = ia.get_next_move(game.board)
            game.make_move(ia.id, next_move)
        else:
            print(game.board)
            valx = input("Enter your x: ")
            valy = input("Enter your y: ")
            game.make_move(1, np.array([int(valx), int(valy)]))
        check = game.check_end()
        turn += 1
    print(game.board)
    if check == ia.id*3:
        print("YOU DIED")
    elif check == 1:
        print("equality")
    else:
        print("my ai loose it SUCK")
    return game


with open('P1_IA.pickle', 'rb') as handle:
    p1_qval = pickle.load(handle)

with open('P2_IA.pickle', 'rb') as handle:
    p2_qval = pickle.load(handle)

p1 = agent.Agent(-1, 1, 1)
p1.q_values = p1_qval
play(p1)
