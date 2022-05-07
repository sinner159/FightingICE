from final_project_code.wrappers.CharacterDataWrapper import CharacterDataWrapper
import final_project_code.action as action
from final_project_code.wrappers.SimulatorWrapper import SimulatorWrapper
from py4j.java_gateway import get_method
from python.feature_extractor.features_extractor import FightingFeaturesExtractor

class State():

    simulatorAdapter: SimulatorWrapper = None

    def __init__(self, frameData = None):
        self.frameData = frameData

        me = self.frameData.getCharacter(False)
        opp = self.frameData.getCharacter(True)
        self.me = CharacterDataWrapper(me)
        self.opp = CharacterDataWrapper(opp)

        self.remainingFrames = self.frameData.getRemainingFramesNumber()
        self.distanceY = self.frameData.getDistanceX()
        self.distanceY = self.frameData.getDistanceY()
        self.framesSinceStart = self.frameData.getFramesNumber()
        self.dequeAtkData = self.frameData.getProjectiles()
        self.dequeAtkDatame = self.frameData.getProjectilesByP1()
        self.dequeAtkDataopp = self.frameData.getProjectilesByP2()
        self.timeSec = self.frameData.getRemainingTime()
        self.timeMill = self.frameData.getRemainingTimeMilliseconds()
        self.roundNum = self.frameData.getRound()
        self.timeRemaining = self.frameData.getRemainingTimeMilliseconds()


    def getLegalActions(self):
        
        if self.me.onGround():
            return action.GROUND_ACTIONS
        
        if self.me.inAir():
            return action.AIR_ACTIONS
        
        #if self.opp.isCrouching():

        return action.ALL_USEFUL_ACTIONS
        
    def isGameOver(self):
        if self.frameData.getEmptyFlag():
            return False

        return self.me.hp <= 0 or self.opp.hp <= 0 or self.timeRemaining <= 0 


    def simulate(self, myActions,oppActions):

        frameData = self.simulatorAdapter.simulateMoves(self.frameData,myActions,oppActions)
        return State(frameData)


    def gameResult(self):
        return 1 if self.me.hp > self.opp.hp else 0
