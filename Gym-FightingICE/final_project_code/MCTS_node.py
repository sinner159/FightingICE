from collections import defaultdict
from final_project_code.action import Action
import numpy as np
from final_project_code.State import State


class MonteCarloTreeSearchNode():
    
    motionDataDict = None
    
    def __init__(self, state, parent=None, parent_action=None):
        self.state: State = state
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self._number_of_visits = 0
        self._results = defaultdict(int)
        self._results[1] = 0
        self._results[-1] = 0

        self.legalActions = Action.ALL_USEFUL_ACTIONS.copy()
        self.l = len(Action.ALL_USEFUL_ACTIONS) - 1
        self.m = 0

        self.ucb = 0
        self.rollout_action_depth = float('inf')
    
    def best_action(self):
        
        simulation_no = 3
        #self.print_children()
        
        for i in range(simulation_no):
            current_node: MonteCarloTreeSearchNode = self._treePolicy()
            reward = current_node.rollout()
            current_node.backpropogate(reward)
        return self.bestChild().parent_action



    def _treePolicy(self):
        
        current_node = self
        
        while not current_node.isTerminalNode():
            
            #change to ShouldExpand() heuristics for expanding or not
            if not current_node.isFullyExpanded():
                return current_node.expand()
            else:
                current_node = current_node.bestChild()
        
        return current_node
    
    def expand(self):
        
        action = self.getUntriedAction()
        next_state = self.state.simulate([action],[])
        child_node = MonteCarloTreeSearchNode(next_state, parent = self, parent_action = action)
        self.children.append(child_node)
        return child_node

    def getUntriedAction(self):

        temp = self.legalActions[self.m] 
                                        #this one should be i
        self.legalActions[self.m] = self.legalActions[self.m] 
        
        #this one should be i too
        self.legalActions[self.m] = temp
        
        self.m += 1

        return self.legalActions[self.m]



    def rollout(self):
        
        current_rollout_state = self.state
        
        myActions = []
        oppActions = []
        rem_frames = current_rollout_state.remainingFrames
        num_actions = 0
        while  rem_frames > 0 and num_actions < self.rollout_action_depth:
            
            possible_moves = current_rollout_state.getLegalActions()
            
            action = self.rollout_policy(possible_moves)
            oppAction = self.rollout_policy(possible_moves)
            
            myActions.append(action)
            oppActions.append(oppAction)
            
            num_actions += 1
            
            actionFN = self.motionDataDict[action].frameNumber
            if rem_frames - actionFN  - 100 < 0:
                break
            rem_frames -= actionFN

        result_state = current_rollout_state.simulate(myActions,oppActions)
        reward = result_state.gameResult(current_rollout_state)
        return reward

    def rollout_policy(self, possible_moves):

        return possible_moves[np.random.randint(len(possible_moves))]
        
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
        return len(self.m) == self.l
    
    def bestChild(self, c_param = .5):
        
        choices_weights = []
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