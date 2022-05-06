from collections import defaultdict
import numpy as np
import time


class MonteCarloTreeSearchNode():
    def __init__(self, state, parent=None, parent_action=None):
        self.state = state
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self._number_of_visits = 0
        self._results = defaultdict(int)
        self._results[1] = 0
        self._results[-1] = 0
        self._untried_actions = None
        self._untried_actions = self.untriedActions()
        return
    
    def untriedActions(self):
        self._untried_actions = self.state.getLegalActions()
        return self._untried_actions
    
    def winsVersusLosses(self):
        wins = self._results[1]
        losses = self._results[-1]
        return wins - losses
    
    def numberOfVisits(self):
        return self._number_of_visits
    
    def expand(self):
        action = self._untried_actions.pop()
        next_state = self.state.move(action)
        child_node = MonteCarloTreeSearchNode(
            next_state, parent = self, parent_action = action)
        
    def isTerminalNode(self):
        return self.state.isGameOver()
    
    def rollout(self):
        current_rollout_state = self.state
        
        while not current_rollout_state.isGameOver():
            possible_moves = current_rollout_state.getLegalActions()
            action = self.rolloutPolicy(possible_moves)
            current_rollout_state = current_rollout_state.move(action)
        return current_rollout_state.gameResult()
    
    def backpropogate(self, result):
        self._number_of_visits += 1.0
        self._results[result] += 1.0
        if self.parent:
            self.parent.backpropogate(result)
            
    def isFullyExpanded(self):
        return len(self._untried_actions) == 0.0
    
    def bestChild(self, c_param = 0.1):
        choices_weights =  [(c.q() / c.n()) + c_param * np.sqrt((2 * np.log(self.n()) / c.n())) for c in self.children]
        return self.children[np.argmax(choices_weights)]
    
    def rollout_policy(self, possible_moves):
        return possible_moves[np.random.randint(len(possible_moves))]
    
    def _treePolicy(self):
        current_node = self
        while not current_node.isTerminalNode():
            if not current_node.isFullyExpanded():
                return current_node.expand()
            else:
                current_node = current_node.bestChild()
        return current_node
    
    def best_action(self):
        simulation_no = 100
        for i in range(simulation_no):
            v = self._treePolicy()
            reward = v.rollout()
            v.backpropagate(reward)
        return self.bestChild(c_param=0.0).parent_action
    
    def get_legal_actions(self): 
        return self.state.getLegalActions()
        
        
    def game_result(self):
        '''
        Modify according to your game or 
        needs. Returns 1 or 0 or -1 depending
        on your state corresponding to win,
        tie or a loss.
        '''
    def move(self,action):
        '''
        Modify according to your game or 
        needs. Changes the state of your 
        board with a new value. For a normal
        Tic Tac Toe game, it can be a 3 by 3
        array with all the elements of array
        being 0 initially. 0 means the board 
        position is empty. If you place x in
        row 2 column 3, then it would be some 
        thing like board[2][3] = 1, where 1
        represents that x is placed. Returns 
        the new state after making a move.
        '''
        
        '''
        EXAMPLE USAGE
        def main():
            root = MonteCarloTreeSearchNode(state = initial_state)
            selected_node = root.best_action()
            return
        '''