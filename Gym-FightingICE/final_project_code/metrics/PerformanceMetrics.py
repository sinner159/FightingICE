


from final_project_code.utils.Logger import Logger


class PerformanceMetrics():

    def __init__(self):
        self.myHp = 0
        self.oppHp = 0
        self.roundLength = 0
        self.roundWon = False
        self.gamesPlayed = 0
        self.oppAIName = ""
        
    
    def write_to_log(self, logger: Logger):
        logger.write(self)


    def __str__(self):
        output = f"""
        MyHP: {self.myHp}
        OppHP: {self.oppHp}
        OppAIName: {self.oppAIName}
        RoundLength: {self.roundLength}
        RoundWon: {self.roundWon}
        OppAIName: {self.oppAIName}
        """
        return output

    def __repr__(self):
        return str(self)
