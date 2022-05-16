


from final_project_code.State import State
from final_project_code.utils.Logger import Logger

class RoundData():
    
    def __init__(self):
        self.myHp = 0
        self.oppHp = 0
        self.roundLength = 0
        self.roundWon = False
        self.gamesPlayed = 0
        self.avg_frames_for_action = 0
        self.total_frames_for_actions = 0
        self.count = 1
        self.hpGap = 0
        
    def getMetrics(self, state: State):
        self.myHp = state.me.hp
        self.oppHp = state.opp.hp
        self.roundLength = 60000 - state.timeRemaining
        self.roundWon = False
        self.hpGap = self.myHp - self.oppHp
        
    def addRunningAvg(self, diffFrames):
        self.total_frames_for_actions += diffFrames
        self.avg_frames_for_action = self.total_frames_for_actions / self.count
        self.count += 1
    
    def write_to_log(self, logger: Logger):
        logger.write(self)

    def __str__(self):
        output = f"""
MyHPLost: {400 - self.myHp}
OppHPLost: {400 -self.oppHp}
HPGap: {self.hpGap}
RoundLength: {self.roundLength}
RoundWon: {self.roundWon}
AvgFramesForAction: {self.avg_frames_for_action}
        """
        return output

    def __repr__(self):
        return str(self)


class PerformanceMetrics():

    def __init__(self, config):
        self.roundData = [RoundData()]
        self.config = config
        self.round = 0
    
    def nextRound(self):
        self.roundData.append(RoundData())
        self.round += 1

    def getMetrics(self,state):
        self.roundData[self.round].getMetrics(state)

    def write_to_log(self, logger: Logger):
        logger.write(f"Config Used: {self.config}")
        self.roundData[self.round].write_to_log(logger)

    def addRunningAvg(self, diffFrames):
        self.roundData[self.round].addRunningAvg(diffFrames)
