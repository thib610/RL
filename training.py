import Tictactoe_class
import Agent_class
from timeit import default_timer as timer
import pickle
from parameters import *
# initialisation of agents
p1 = Agent_class.Agent(-1)
p2 = Agent_class.Agent(1)

# training of agents
start = timer()
for i in range(0, nb_games):
    if i % 1000 == 0:
        print(i)
    Tictactoe_class.ia_versus(p1, p2)
end = timer()
print("training time", end - start)

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
