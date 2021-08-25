import Tictactoe_class
import Agent
from timeit import default_timer as timer
import pickle

# Variable of the algorithm
init = 0.5
lr = 0.5
epsilon_greed = 0.85
nb_games = 1000000

# initialisation of agents
p1 = Agent.Agent(-1, epsilon_greed, lr)
p2 = Agent.Agent(1, epsilon_greed, lr)

# training of agents
start = timer()
for i in range(0, nb_games):
    if i % 1000 == 0:
        print(i)
    Tictactoe_class.play(p1, p2, init)
end = timer()
print(end - start)

# save q_values of agents, check
# p1 agent
with open('P1_IA.pickle', 'wb') as handle:
    pickle.dump(p1.q_values, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('P1_IA.pickle', 'rb') as handle:
    p1_qval = pickle.load(handle)
print(p1.q_values == p1_qval)

# p2 agent
with open('P2_IA.pickle', 'wb') as handle:
    pickle.dump(p2.q_values, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('P2_IA.pickle', 'rb') as handle:
    p2_qval = pickle.load(handle)
print(p2.q_values == p2_qval)
