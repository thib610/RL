import classes.Tictactoe_class
import pickle
import classes.Agent_class

# load IA saved
with open('agent_model/P1_IA.pickle', 'rb') as handle:
    p1_qval = pickle.load(handle)

with open('agent_model/P2_IA.pickle', 'rb') as handle:
    p2_qval = pickle.load(handle)

# initialisation of the agent
# -1 id of the agent, 1 epsilon (choose only bes move), 1 placeholder
p1 = classes.Agent_class.Agent(-1)
p1.q_values = p1_qval

# launch of the game
classes.Tictactoe_class.ia_vs_human(p1)
