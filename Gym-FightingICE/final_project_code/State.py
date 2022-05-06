from .action import ALL_USEFUL_ACTIONS
from final_project_code.wrappers.SimulatorWrapper import SimulatorWrapper
from py4j.java_gateway import get_method
from python.feature_extractor.features_extractor import FightingFeaturesExtractor

class State():

    simulatorAdapter: SimulatorWrapper = None

    def __init__(self, frameData = None):
        self.frameData = frameData

    def getLegalActions(self):
        return ALL_USEFUL_ACTIONS
        
    def isGameOver(self):
        if self.frameData.getEmptyFlag():
            return False

        rem = self.frameData.getRemainingFramesNumber()
        p1 = self.frameData.getCharacter(False)
        p2 = self.frameData.getCharacter(True)
        distanceY = self.frameData.getDistanceX()
        distanceY = self.frameData.getDistanceY()
        framesSinceStart = self.frameData.getFramesNumber()
        dequeAtkData = self.frameData.getProjectiles()
        dequeAtkDataP1 = self.frameData.getProjectilesByP1()
        dequeAtkDataP2 = self.frameData.getProjectilesByP2()
        timeSec = self.frameData.getRemainingTime()
        timeMill = self.frameData.getRemainingTimeMilliseconds()
        roundNum = self.frameData.getRound()
        p1Hp = p1.getHp()
        p2Hp = p2.getHp()
        timeRemaining = self.frameData.getRemainingTimeMilliseconds()

        return p1Hp <= 0 or p2Hp <= 0 or timeRemaining <= 0 


    def move(self, action):
        frameData = self.simulatorAdapter.simulateMove(self.frameData,[action],[])
        return State(frameData)

    def gameResult(self):
        p1Hp = self.frameData.getCharacter(False).getHp()
        p2Hp = self.frameData.getCharacter(True).getHp()

        return 1 if p1Hp > p2Hp else 0
