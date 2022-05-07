


from final_project_code.State import State
from final_project_code.utils.Logger import Logger


class PerformanceMetrics():

    def __init__(self):
        self.myHp = 0
        self.oppHp = 0
        self.roundLength = 0
        self.roundWon = False
        self.gamesPlayed = 0
        
    
    def getMetrics(self, state: State):
        self.myHp = state.me.hp
        self.oppHp = state.opp.hp
        self.roundLength = 60000 - state.timeMill
        self.roundWon = False
        
    
    def write_to_log(self, logger: Logger):
        logger.write(self)


    def __str__(self):
        output = f"""
        MyHP: {self.myHp}
        OppHP: {self.oppHp}
        RoundLength: {self.roundLength}
        RoundWon: {self.roundWon}
        """
        return output

    def __repr__(self):
        return str(self)
