from final_project_code.Actions import ActionsSingleArray
from final_project_code.wrappers.CharacterDataWrapper import CharacterDataWrapper
import final_project_code.action as action
from final_project_code.wrappers.SimulatorWrapper import SimulatorWrapper
from py4j.java_gateway import get_method
from python.feature_extractor.features_extractor import FightingFeaturesExtractor

class State():

    def __init__(self, frameData = None):
        
        self.frameData = frameData

        self.me = CharacterDataWrapper(self.frameData.getCharacter(True))
        self.opp = CharacterDataWrapper(self.frameData.getCharacter(False))

        self.distanceY = self.frameData.getDistanceX()
        self.distanceY = self.frameData.getDistanceY()
        self.framesSinceStart = self.frameData.getFramesNumber()
        self.dequeAtkData = self.frameData.getProjectiles()
        self.dequeAtkDatame = self.frameData.getProjectilesByP1()
        self.dequeAtkDataopp = self.frameData.getProjectilesByP2()
        self.roundNum = self.frameData.getRound()
        self.timeRemaining = self.frameData.getRemainingTimeMilliseconds()
        self.remainingFrames = self.frameData.getRemainingFramesNumber()

        self.actions:ActionsSingleArray = ActionsSingleArray()
        
    def isGameOver(self):
        if self.frameData.getEmptyFlag():
            return False

        return self.me.hp <= 0 or self.opp.hp <= 0 or self.timeRemaining <= 0 


    def getUnusedAction(self):
        return self.actions.getUnusedAction()

    
    def gameResult(self, starting_state: "State"):
        deltaMyHp = (self.me.hp - starting_state.me.hp)
        deltaOppHp = (self.opp.hp - starting_state.opp.hp)
        return 1 if deltaMyHp > deltaOppHp else 0
        #return 1 if self.me.hp > self.opp.hp else 0
