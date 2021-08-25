import Tictactoe_class
import pickle
import Agent

# load IA saved
with open('P1_IA.pickle', 'rb') as handle:
    p1_qval = pickle.load(handle)

with open('P2_IA.pickle', 'rb') as handle:
    p2_qval = pickle.load(handle)

# initialisation of the agent
# -1 id of the agent, 1 epsilon (choose only bes move), 1 placeholder
p1 = Agent.Agent(-1, 1, 1)
p1.q_values = p1_qval

# launch of the game
Tictactoe_class.ia_vs_human(p1)
