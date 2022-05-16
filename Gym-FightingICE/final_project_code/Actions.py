from final_project_code.action import ALL_USEFUL_ACTIONS
import numpy as np

class ActionsSingleArray():
    
    legalActions = None
    legalOppActions = ALL_USEFUL_ACTIONS.copy()
    
    def __init__(self):
        self.l = len(self.legalActions) - 1
        self.m = 0

    def getUnusedAction(self):
        
        i = 0
        if self.m + 1 == self.l:
            i = self.l
        else:
            i = np.random.randint(self.m + 1,self.l)

        #temp is stand
        temp = self.legalActions[self.m] 
        #m is whatever random action
        self.legalActions[self.m] = self.legalActions[i] 
        #i is stand
        self.legalActions[i] = temp

        ret = self.legalActions[self.m]
        self.m += 1
        
        return ret

    def isFullyExpanded(self):
        return self.m == self.l