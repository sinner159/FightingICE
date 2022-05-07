from final_project_code.action import ALL_USEFUL_ACTIONS

class ActionsSingleArray():

    def __init__(self):
        self.legalActions = ALL_USEFUL_ACTIONS.copy()
        self.l = len(ALL_USEFUL_ACTIONS) - 1
        self.m = 0

    def getUnusedAction(self):

        temp = self.legalActions[self.m] 
                                        #this one should be i
        self.legalActions[self.m] = self.legalActions[self.m] 
        
        #this one should be i too
        self.legalActions[self.m] = temp
        
        self.m += 1

        return self.legalActions[self.m]

    def isFullyExpanded(self):
        return self.m == self.l