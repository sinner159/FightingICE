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
    
    def __init__(self, state,treePolicy: TreePolicy = None, rolloutPolicy: RolloutPolicy = None, parent=None, parent_action=None):
        self.state: State = state
        
        if treePolicy != None:
            self.treePolicy  = treePolicy
        
        if rolloutPolicy != None:
            self.rolloutPolicy = rolloutPolicy

        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self._number_of_visits = 0
        self._results = defaultdict(int)
        self._results[1] = 0
        self._results[-1] = 0
        
        self.ucb = 0
        self.simulationFrameLimit = 50

        self.budget = 14 #16.67
    
    def best_action(self):
        
        #self.print_children()
        
        start = time.time()
        while time.time() - start < self.budget:
            startLoop = time.time()
            current_node: MonteCarloTreeSearchNode = self.treePolicy.getNode(self)
            reward = current_node.rollout()
            current_node.backpropogate(reward)
            print(f"Took {time.time() - startLoop} sec")

        return self.bestChild().parent_action
        
    
    def expand(self):
        
        action = self.state.getUnusedAction()
        next_state = self.state.simulate([action],[])
        child_node = MonteCarloTreeSearchNode(next_state, parent = self, parent_action = action, treePolicy=self.treePolicy, rolloutPolicy=self.rolloutPolicy)
        self.children.append(child_node)
        return child_node

    def rollout(self):
        
        current_rollout_state = self.state
        
        myActions = []
        oppActions = []
        
        totalFrames = 0
        while  True:
            
            possible_moves = current_rollout_state.actions.legalActions
            
            action = self.rolloutPolicy.getNode(possible_moves)
            oppAction = self.rolloutPolicy.getNode(possible_moves)

            actionFrameNum = self.motionDataDict[action].frameNumber

            if actionFrameNum + totalFrames > self.simulationFrameLimit:
                break
            
            totalFrames += actionFrameNum
            myActions.append(action)
            oppActions.append(oppAction)
            
        result_state = current_rollout_state.simulate(myActions,oppActions)
        reward = result_state.gameResult(current_rollout_state)
        return reward

    def backpropogate(self, result):
        
        self._number_of_visits += 1.0
        self._results[result] += 1.0
        if self.parent:
            self.parent.backpropogate(result)
    
    def winsVersusLosses(self):
        
        wins = self._results[1]
        losses = self._results[-1]
        return wins - losses
    
    def wins(self):
        wins = self._results[1]
        return wins

    def numberOfVisits(self):
        return self._number_of_visits
    
    def isTerminalNode(self):
        return self.state.isGameOver()
    
    def isFullyExpanded(self):
        return self.state.actions.isFullyExpanded()
    
    def bestChild(self, c_param = 1.4):
        
        choices_weights = []

        c:MonteCarloTreeSearchNode
        for c in self.children:
            wins = c.wins()
            numVisits =  c.numberOfVisits()
            c.ucb = (wins/numVisits) + c_param * np.sqrt(np.log2(numVisits) / numVisits)
            choices_weights.append(c.ucb)
            
        child_node = self.children[np.argmax(choices_weights)]
        return child_node

    def __str__(self):
        return f"Action: {self.parent_action} Wins: {self.wins()} #_Vis {self.numberOfVisits()} UCB {self.ucb}"
    
    def __repr__(self):
        return str(self)
  
    def print_children(self):
        print("************Children*************")
        for c in self.children:
            print(c)
        print("************END*************")