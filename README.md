Gym-FightingICE/final_project_code contains all of our essential code. Everything outside of this folder, with the exception of a couple of test files,is from the FightingICE team. 

In our folder:

TestAI.py is our agent

MCTS_node.py is MCTS this uses RolloutPolicy and TreePolicy found in their respective files

GAExperiments and Experiments are what we used to automate the running of our tests. They both use GameStarter, to run the game with our configuration

Everything in the wrappers folder was created to make manipulated the Java objects easier as we could not see any info in the debugger unless it was converted to a python object

All or most of the data that we used for our results can be found in the logs folder