from .action import ALL_USEFUL_ACTIONS
from final_project_code.wrappers.SimulatorWrapper import SimulatorAdapter
from py4j.java_gateway import get_method
from python.feature_extractor.features_extractor import FightingFeaturesExtractor

class State():

    simulatorAdapter: SimulatorAdapter = None

    def __init__(self, frameData = None):
        self.frameData = frameData

    def getLegalActions(self):
        return ALL_USEFUL_ACTIONS
        
    def isGameOver(self):

        p1 = self.frameData.getCharacter(False)
        p2 = self.frameData.getCharacter(True)
        p1Hp = FightingFeaturesExtractor.get_hp(self.frameData,"P1")
        p2Hp = FightingFeaturesExtractor.get_hp(self.frameData,"P2")
        #p1Hp = get_method(p1,"getHp()")
        #p2Hp = get_method(p2,"getHp()")
        timeRemaining = self.frameData.getRemainingTimeMilliseconds()

        return p1Hp <= 0 or p2Hp <= 0 or timeRemaining <= 0 


    def move(self, action):
        return State(self.simulatorAdapter.simulateMove(list(action)))

    def gameResult(self):
        p1Hp = self.frameData.getCharacter(False).getHp()
        p2Hp = self.frameData.getCharacter(True).getHp()

        return 1 if p1Hp > p2Hp else 0
