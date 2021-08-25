import random
import Tictactoe_class
import agent
from timeit import default_timer as timer
import pickle

def play(p1, p2):
    turn = random.randint(0, 1)
    game = Tictactoe_class.Tictactoe()
    check = 0
    while check == 0:
        if turn % 2 == 0:
            next_move = p1.get_next_move(game.board)
            p1.add_state(game.board, next_move, init)
            game.make_move(-1, next_move)
        else:
            next_move = p2.get_next_move(game.board)
            p2.add_state(game.board, next_move, init)
            game.make_move(1, next_move)
        check = game.check_end()
        turn += 1
    p1.update_q_values(check)
    p2.update_q_values(check)
    p1.rest_historic()
    p2.rest_historic()
    return game


init = 0.5
lr = 0.5
epsilon_greed = 0.85

p1 = agent.Agent(-1, epsilon_greed, lr)
p2 = agent.Agent(1, epsilon_greed, lr)

start = timer()

for i in range(0, 1):
    if i % 1000 == 0:
        print(i)
    play(p1, p2)
end = timer()
print(end - start)


with open('P1_IA.pickle', 'wb') as handle:
    pickle.dump(p1.q_values, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('P1_IA.pickle', 'rb') as handle:
    p1_qval = pickle.load(handle)
print(p1.q_values == p1_qval)


with open('P2_IA.pickle', 'wb') as handle:
    pickle.dump(p2.q_values, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('P2_IA.pickle', 'rb') as handle:
    p2_qval = pickle.load(handle)
print(p2.q_values == p2_qval)
