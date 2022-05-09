from collections import deque
from time import time
from final_project_code.MCTS_node import MonteCarloTreeSearchNode
from final_project_code.RolloutPolicy import RolloutPolicy
from final_project_code.TreePolicy import TreePolicy
from final_project_code.metrics.PerformanceMetrics import PerformanceMetrics
from final_project_code.utils.Logger import Logger
from final_project_code.wrappers.SimulatorWrapper import SimulatorWrapper
from py4j.java_gateway import get_field
from .State import State

class TestAI(object):

    motionDataDict = {}

    def __init__(self, gateway, performanceMetrics: PerformanceMetrics, logger: Logger):
        self.gateway = gateway
        self.performanceMetrics = performanceMetrics
        self.logger = logger
        
    def close(self):
        pass
        
    
    # Gets information from the game status in each frame. <br>
	#  * Such information is stored in the parameter frameData. <br>
	#  * If {@code frameData.getRemainingTime()} returns a negative value, the
	#  * current round has not started yet. <br>
	#  * When you use frameData received from getInformation(), <br>
	#  * you must always check if the condition
	#  * {@code !frameData.getEmptyFlag() && frameData.getRemainingTime() > 0}
	#  * holds; otherwise, NullPointerException will occur. <br>
	#  * You must also check the same condition when you use the CommandCenter
	#  * class.
    # @param fd
	#  *            the data that will be changed each frame
	#  * @param isControl
	#  *            whether the character can act. this parameter is not delayed
	#  *            unlike {@link struct.CharacterData#isControl()}
    def getInformation(self, frameData, isControl):
        # Getting the frame data of the current frame
        self.frameData = frameData
        self.cc.setFrameData(self.frameData, self.player)

    # please define this method when you use FightingICE version 3.20 or later
    def roundEnd(self, x, y, z):
        self.logger.write(str(self.performanceMetrics))
        endState = State(self.frameData)
        self.performanceMetrics.getMetrics(endState)
        self.logger.write(self.performanceMetrics)
        
    	
    # please define this method when you use FightingICE version 4.00 or later
    def getScreenData(self, sd):
        pass
        
    def initialize(self, gameData, player):
        # Initializng the command center, the simulator and some other things
        self.inputKey = self.gateway.jvm.struct.Key()
        self.frameData = self.gateway.jvm.struct.FrameData()
        self.cc = self.gateway.jvm.aiinterface.CommandCenter()
        
        self.player = player
        self.gameData = gameData
        myMotionDataList = gameData.getMotionData(False)

        for motionData in myMotionDataList:
            self.motionDataDict[motionData.actionName] = motionData

        self.mcts_root = None
        State.simulatorAdapter = SimulatorWrapper(self.gateway, self.gameData.getSimulator(), self.motionDataDict)
        self.lastTime = time()
        return 0
        
    def input(self):
        # Return the input for the current frame
        return self.inputKey
        
    def processing(self):
        #compute the input for the current frame
        #================================
        diff = time() - self.lastTime
        #print("diff was" + str(diff))

        if self.frameData.getEmptyFlag() or self.frameData.getRemainingFramesNumber() <= 0:
                self.isGameJustStarted = True
                return

        if self.mcts_root == None:
            self.mcts_root = MonteCarloTreeSearchNode(State(self.frameData),TreePolicy(),RolloutPolicy())
            MonteCarloTreeSearchNode.motionDataDict = self.motionDataDict
        #SkillFlag tells us whether or not we're still executing a skill. 
        # True when queue of inputs waiting to be executed for the skill
        if self.cc.getSkillFlag():
                self.inputKey = self.cc.getSkillKey()
                return
        
        action = self.mcts_root.best_action()
        print(action)
        self.inputKey.empty()
        
        self.cc.commandCall(action)
        self.lastTime = time()
      
                        
    # This part is mandatory
    class Java:
        implements = ["aiinterface.AIInterface"]
        


    