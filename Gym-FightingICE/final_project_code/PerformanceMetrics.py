


from final_project_code.State import State
from final_project_code.utils.Logger import Logger

class RoundData():
    
    def __init__(self, maxHP):
        self.myHp = 0
        self.oppHp = 0
        self.roundLength = 0
        self.roundWon = False
        self.gamesPlayed = 0
        self.avg_frames_for_action = 0
        self.total_frames_for_actions = 0
        self.count = 1
        self.hpGap = 0
        self.maxHP = maxHP
        
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
MyHPLost: {self.maxHP - self.myHp}
OppHPLost: {self.maxHP - self.oppHp}
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
        self.config = config
        self.roundData = [RoundData(self.config.maxHP)]
        self.round = 0
    
    def nextRound(self):
        self.roundData.append(RoundData(self.config.maxHP))
        self.round += 1


    def getMetrics(self,state):
        self.roundData[self.round].getMetrics(state)


    def write_to_log(self, logger: Logger):
        logger.write(f"Config Used: {self.config}")
        i = 1
        avgRound = RoundData(self.config.maxHP)
        for round in self.roundData:
            logger.write(f"Round {i}")
            round.write_to_log(logger)
            avgRound.myHp += round.myHp
            avgRound.oppHp += round.oppHp
            avgRound.roundLength += round.roundLength
            avgRound.roundWon += round.roundWon
            avgRound.hpGap += round.hpGap
            avgRound.avg_frames_for_action += round.avg_frames_for_action
            i+=1

        avgRound.myHp /= i
        avgRound.oppHp /= i
        avgRound.roundLength /= i
        avgRound.roundWon /= i
        avgRound.hpGap /= i
        avgRound.avg_frames_for_action /= i

        logger.write("Average:\n")
        avgRound.write_to_log(logger)


    def addRunningAvg(self, diffFrames):
        self.roundData[self.round].addRunningAvg(diffFrames)

