from .action import Action, ALL_USEFUL_ACTIONS


class State():

    simulator = None

    def __init__(self, frameData = None):
        self.frameData = frameData
        self.simulator = simulator

    def getLegalActions(self):
        return ALL_USEFUL_ACTIONS
        
    def isGameOver(self):
        return False

#simulate(FrameData frameData, 
# boolean playerNumber, 
# java.util.Deque<Action> myAct, 
# java.util.Deque<Action> oppAct, 
# int simulationLimit)
    def move(self, action):
        frameData = self.simulator.simulate(self.frameData,True,None, None, 1)
        return State(frameData)