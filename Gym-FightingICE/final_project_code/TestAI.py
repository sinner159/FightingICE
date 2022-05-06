from collections import deque
from final_project_code.MCTS_node import MonteCarloTreeSearchNode
from final_project_code.wrappers.SimulatorWrapper import SimulatorWrapper
from py4j.java_gateway import get_field
from .State import State

class TestAI(object):
    def __init__(self, gateway):
        self.gateway = gateway
        
        
    def close(self):
        pass
        
    def getInformation(self, frameData, isControl):
        # Getting the frame data of the current frame
        self.frameData = frameData

        self.cc.setFrameData(self.frameData, self.player)


    # please define this method when you use FightingICE version 3.20 or later
    def roundEnd(self, x, y, z):
    	print(x)
    	
    # please define this method when you use FightingICE version 4.00 or later
    def getScreenData(self, sd):
    	a=0
        
    def initialize(self, gameData, player):
        # Initializng the command center, the simulator and some other things
        self.inputKey = self.gateway.jvm.struct.Key()
        self.frameData = self.gateway.jvm.struct.FrameData()
        self.cc = self.gateway.jvm.aiinterface.CommandCenter()
        
        self.player = player
        self.gameData = gameData
        self.mcts_root = None
        State.simulatorAdapter = SimulatorWrapper(self.gateway, self.gameData.getSimulator())
        return 0
        
    def input(self):
        # Return the input for the current frame
        return self.inputKey
        
    def processing(self):
        #compute the input for the current frame
        #================================
        if self.frameData.getEmptyFlag() or self.frameData.getRemainingFramesNumber() <= 0:
                self.isGameJustStarted = True
                return

        if self.mcts_root == None:
            self.mcts_root = MonteCarloTreeSearchNode(State(self.frameData))

        #SkillFlag tells us whether or not we're still executing a skill. 
        # True when queue of inputs waiting to be executed for the skill
        if self.cc.getSkillFlag():
                self.inputKey = self.cc.getSkillKey()
                return
        
        action = self.mcts_root.best_action()

        self.inputKey.empty()
        #============================
        #Start processing
        # Just spam kick
        
        self.cc.commandCall(action)
      
                        
    # This part is mandatory
    class Java:
        implements = ["aiinterface.AIInterface"]
        


    