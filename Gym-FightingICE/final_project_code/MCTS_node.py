from collections import defaultdict
from email import policy
import time
from final_project_code.RolloutPolicy import RolloutPolicy
from final_project_code.TreePolicy import TreePolicy
from final_project_code.action import Action
import numpy as np
from final_project_code.State import State


class MonteCarloTreeSearchNode():
    
    motionDataDict = None
    
    def __init__(self, state,c_param, num_simulations, treePolicy: TreePolicy = None, rolloutPolicy: RolloutPolicy = None, parent=None, parent_action=None):
        self.state: State = state
        
        if treePolicy != None:
            self.treePolicy  = treePolicy
        
        if rolloutPolicy != None:
            self.rolloutPolicy = rolloutPolicy

        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self.number_of_visits = 0
        self.totalReward = 0
        self.ucb = 0
        self.c_param = c_param
        self.num_simulations = num_simulations
    
    def best_action(self):
        
        self.totalReward = 0
        #self.print_children()
        
        # start = time.time()
        # while time.time() - start < self.budget:
        #     startLoop = time.time()
        for i in range(self.num_simulations):
            current_node: MonteCarloTreeSearchNode = self.treePolicy.getNode(self)
            reward = self.rolloutPolicy.rollout(current_node)
            current_node.backpropogate(reward)
            #print(f"Took {time.time() - startLoop} sec")

        return self.bestChild().parent_action
        
    
    def expand(self):
        
        action = self.state.getUnusedAction()
        next_state = self.rolloutPolicy.simulateOneMove(self.state.frameData, action)

        child_node = MonteCarloTreeSearchNode(next_state,self.c_param, self.num_simulations, parent = self, parent_action = action, treePolicy=self.treePolicy, rolloutPolicy=self.rolloutPolicy)
        self.children.append(child_node)
        return child_node

    def backpropogate(self, reward):
        
        self.number_of_visits += 1.0
        self.totalReward += reward
        if self.parent:
            self.parent.backpropogate(reward)

    def isTerminalNode(self):
        return self.state.isGameOver()
    
    def isFullyExpanded(self):
        return self.state.actions.isFullyExpanded()
    
    def bestChild(self):
        
        choices_weights = []

        c:MonteCarloTreeSearchNode
        for c in self.children:
            c.ucb = (c.totalReward/c.number_of_visits) + self.c_param * np.sqrt(np.log2(self.number_of_visits) / c.number_of_visits)
            choices_weights.append(c.ucb)
            
        child_node = self.children[np.argmax(choices_weights)]
        return child_node

    def __str__(self):
        return f"Action: {self.parent_action} Wins: {self.totalReward} #_Vis {self.number_of_visits} UCB {self.ucb}"
    
    def __repr__(self):
        return str(self)
  
    def print_children(self):
        print("************Children*************")
        for c in self.children:
            print(c)
        print("************END*************")