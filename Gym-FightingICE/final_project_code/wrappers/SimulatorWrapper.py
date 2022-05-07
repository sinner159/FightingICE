from final_project_code.wrappers.GatewayWrapper import GatewayWrapper


class SimulatorWrapper(GatewayWrapper):

    def __init__(self, gateway, simulator, motionDataDict):
        super().__init__(gateway)
        self.simulator = simulator
        self.motionDataDict = motionDataDict

#simulate(FrameData frameData, boolean playerNumber, java.util.Deque<Action> myAct, java.util.Deque<Action> oppAct, int simulationLimit)
    def simulateMoves(self,frameDataBefore, myActions, oppActions):

        sumFrames = self.getTotalFrames(myActions)

        myActionsJava = self.getDeque(myActions)
        oppActionsJava = self.getDeque(oppActions)
        

        frameDataAfter = self.simulator.simulate(frameDataBefore,True, myActionsJava, oppActionsJava, sumFrames)
        return frameDataAfter

    def getTotalFrames(self, myActions):
        
        sumFrames = 0
        for action in myActions:
            sumFrames += self.motionDataDict[action].frameNumber        
            
        return sumFrames