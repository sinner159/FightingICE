from final_project_code.wrappers.GatewayWrapper import GatewayWrapper
import time


class SimulatorWrapper(GatewayWrapper):

    def __init__(self, gateway, simulator, motionDataDict, simulationFrameLimit):
        super().__init__(gateway)
        self.simulator = simulator
        self.motionDataDict = motionDataDict
        self.simulationFrameLimit = simulationFrameLimit

#simulate(FrameData frameData, boolean playerNumber, java.util.Deque<Action> myAct, java.util.Deque<Action> oppAct, int simulationLimit)
    def simulate(self,frameDataBefore, myActions, oppActions, totalFrames):
        myActionsJava = self.getDeque(myActions)
        oppActionsJava = self.getDeque(oppActions)
        
        frameDataAfter = self.simulator.simulate(frameDataBefore,True, myActionsJava, oppActionsJava, totalFrames)
        return frameDataAfter

    def simulateOneMove(self, frameData, actions):
        myActions = actions
        myActionsJava = self.getDeque(myActions)
        totalFrames = self.getTotalFrames(myActions)

        frameDataAfter = self.simulator.simulate(frameData,True, myActionsJava, self.getDeque([]), totalFrames)
        return frameDataAfter

    def getFrameNumber(self, action):
        return self.motionDataDict[action].frameNumber

    def getTotalFrames(self, myActions):
        
        sumFrames = 0
        for action in myActions:
            sumFrames += self.motionDataDict[action].frameNumber        
            
        return sumFrames