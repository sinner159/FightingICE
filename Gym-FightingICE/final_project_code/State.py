from final_project_code.wrappers.CharacterDataWrapper import CharacterDataWrapper
from .action import ALL_USEFUL_ACTIONS
from final_project_code.wrappers.SimulatorWrapper import SimulatorWrapper
from py4j.java_gateway import get_method
from python.feature_extractor.features_extractor import FightingFeaturesExtractor

class State():

    simulatorAdapter: SimulatorWrapper = None

    def __init__(self, frameData = None):
        self.frameData = frameData

        p1 = self.frameData.getCharacter(False)
        p2 = self.frameData.getCharacter(True)
        self.p1 = CharacterDataWrapper(p1)
        self.p2 = CharacterDataWrapper(p2)

        self.rem = self.frameData.getRemainingFramesNumber()
        self.distanceY = self.frameData.getDistanceX()
        self.distanceY = self.frameData.getDistanceY()
        self.framesSinceStart = self.frameData.getFramesNumber()
        self.dequeAtkData = self.frameData.getProjectiles()
        self.dequeAtkDataP1 = self.frameData.getProjectilesByP1()
        self.dequeAtkDataP2 = self.frameData.getProjectilesByP2()
        self.timeSec = self.frameData.getRemainingTime()
        self.timeMill = self.frameData.getRemainingTimeMilliseconds()
        self.roundNum = self.frameData.getRound()
        self.timeRemaining = self.frameData.getRemainingTimeMilliseconds()




    def getLegalActions(self):

        
        return ALL_USEFUL_ACTIONS
        
    def isGameOver(self):
        if self.frameData.getEmptyFlag():
            return False

        return self.p1.hp <= 0 or self.p2.hp <= 0 or self.timeRemaining <= 0 


    def move(self, action):
        frameData = self.simulatorAdapter.simulateMove(self.frameData,[action],[])
        return State(frameData)

    def gameResult(self):
        p1Hp = self.frameData.getCharacter(False).getHp()
        p2Hp = self.frameData.getCharacter(True).getHp()

        return 1 if p1Hp > p2Hp else 0
