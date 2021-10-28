# Tictactoe with reinforcment learning
## requirement
* pickle 
* timeit
* numpy
* random
* copy
* math 



## Files
### RL folder:
### parameters.py
Contains parameters of the algorithm.
### training.py
Run this file to launch the training, it will automaticly update the 2 pickle files.  

### pve.py
run this file to play against an IA.
### classes folder :
#### Agent_class.py
file contain the agent class. An object of this class is an IA, after the initialisaton the IA must be train.  

#### Tictactoe_class.py
this class is use to play the game. 

### Agent_model folder :
#### P1_IA.pickle
contain the q_table of the agent 1.
basicly it contain the IA number one.

#### P2_IA.pickle
contain the q_table of the agent 2.
basicly it contain the IA number one.

## HOW TO PLAY AGAINST IA (pvp will be implement one day, maybe):
### Begining
At each begning of turn the the board will be print in the console like this:  
////// terminal exemple //////  
IA token: -1  
your token: 1  
[[ 0.  0.  0.]  
 [ 0.  0.  0.]  
 [-1.  0.  0.]]  
////// terminal exemple //////  
 note: (here the IA start first, the order of player is random)  
 
 ### Make a move
To make a move you'll need to input the x coordinate first then the y coordinate.  

Enter your x: 1  
Enter your y: 1  
the coordinate (1,1) will make a move in the top left corner  
the coordinate (3,3) will make a move in the bottom right corner  

### Exemple
here an exemple of the begining of a game:  
////// terminal exemple //////  
IA token: -1  
your token: 1  
[[ 0.  0.  0.]  
 [ 0.  0.  0.]  
 [-1.  0.  0.]]  
Enter your x: 1  
Enter your y: 1  
[[ 1.  0. -1.]  
 [ 0.  0.  0.]  
 [-1.  0.  0.]]  
Enter your x: 2  
Enter your y: 2  
[[ 1.  0. -1.]  
 [ 0.  1.  0.]  
 [-1.  0. -1.]]  
////// terminal exemple //////  
 
