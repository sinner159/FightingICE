from time import time
from final_project_code.Actions import ActionsSingleArray
from final_project_code.MCTS_node import MonteCarloTreeSearchNode
from final_project_code.RolloutPolicy import RolloutPolicy
from final_project_code.TreePolicy import TreePolicy
from final_project_code.PerformanceMetrics import PerformanceMetrics
from final_project_code.utils.Logger import Logger
from final_project_code.wrappers.SimulatorWrapper import SimulatorWrapper
from final_project_code.wrappers.MotionDataWrapper import MotionDataWrapper
from .State import State

class TestAI(object):

    motionDataDict = {}

    def __init__(self, gateway, config, logger):
        self.gateway = gateway
        self.logger = logger
        self.config = config
        self.performanceMetrics = PerformanceMetrics(self.config)
        State.eval_function = self.config.eval_function
        ActionsSingleArray.legalActions = self.config.action_set
        self.currentRound = 1
        
        
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



    #This frame is from 15 frames ago
    def getInformation(self, frameData, isControl):
        # Getting the frame data of the current frame
        self.isControl = isControl
        self.frameData = frameData
        if not self.frameData.getEmptyFlag():
            self.state = State(self.frameData)
            
                

        self.cc.setFrameData(self.frameData, self.player)


    # please define this method when you use FightingICE version 3.20 or later
    def roundEnd(self, x, y, z):
        if not self.frameData.getEmptyFlag():
            endState = State(self.frameData)
            self.performanceMetrics.getMetrics(endState)
            self.lastFrameNumber = 0
            
        
    	
    # please define this method when you use FightingICE version 4.00 or later
    def getScreenData(self, sd):
        pass
        
    def initialize(self, gameData, player):
        # Initializng the command center, the simulator and some other things
        self.inputKey = self.gateway.jvm.struct.Key()
        self.frameData = self.gateway.jvm.struct.FrameData()
        self.cc = self.gateway.jvm.aiinterface.CommandCenter()
        self.isControl = True
        self.player = player
        self.gameData = gameData
        myMotionDataList = gameData.getMotionData(False)

        for motionData in myMotionDataList:
            self.motionDataDict[motionData.actionName] = MotionDataWrapper(motionData)

        self.mcts_root = None
        self.lastFrameNumber = 0
        self.lastTime = time()
        return 0
        
    def input(self):
        # Return the input for the current frame
        # #print(self.inputKey.A)
        #print(f"A: {self.inputKey.A} B: {self.inputKey.B} C: {self.inputKey.C} D: {self.inputKey.D} L: {self.inputKey.L} R: {self.inputKey.R} U: {self.inputKey.U}")
        return self.inputKey
        
    def processing(self):
        #compute the input for the current frame
        #================================
        
        #print(f"isControl: {self.isControl}")
        frameEmpty= self.frameData.getEmptyFlag()
        #print(f"frameEmpty: {frameEmpty} FrameNumber: {self.frameData.getFramesNumber()}  RemFrames: {self.frameData.getRemainingFramesNumber()}")
        if frameEmpty or self.frameData.getRemainingFramesNumber() <= 0:
                self.isGameJustStarted = True
                return

        if self.mcts_root == None:
            self.rolloutPolicy = RolloutPolicy(SimulatorWrapper(self.gateway, self.gameData.getSimulator(), self.motionDataDict, self.config.simulation_limt))
            
        if self.state.roundNum > self.currentRound:
            self.currentRound = self.state.roundNum
            self.performanceMetrics.nextRound()
        
        #SkillFlag tells us whether or not we're still executing a skill. 
        # True when queue of inputs waiting to be executed for the skill
        flag = self.cc.getSkillFlag()
        #print(f"getSkillFlag is: {flag}")
        if flag:
                self.inputKey = self.cc.getSkillKey()
                return

        self.inputKey.empty()
        #self.cc.skillCancel()
        
        self.mcts_root = MonteCarloTreeSearchNode(State(self.frameData), self.config.c_param,self.config.num_simulations, TreePolicy(),self.rolloutPolicy)
        action = self.mcts_root.best_action()
        
        diffFrames = self.state.framesSinceStart - self.lastFrameNumber
        self.lastFrameNumber = self.state.framesSinceStart
        self.performanceMetrics.addRunningAvg(diffFrames)
        
        
        self.cc.commandCall(action)
        #print(f"Action: {action} FrameNum: {self.state.framesSinceStart}")

        
    # This part is mandatory
    class Java:
        implements = ["aiinterface.AIInterface"]
        


    