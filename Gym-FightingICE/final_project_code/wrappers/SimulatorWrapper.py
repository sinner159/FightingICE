from final_project_code.wrappers.GatewayWrapper import GatewayWrapper


class SimulatorWrapper(GatewayWrapper):

    def __init__(self, gateway, simulator):
        super().__init__(gateway)
        self.simulator = simulator

#simulate(FrameData frameData, boolean playerNumber, java.util.Deque<Action> myAct, java.util.Deque<Action> oppAct, int simulationLimit)
    def simulateMove(self,frameDataBefore, p1Actions, p2Actions):

        p1ActionsJava = self.getDeque(p1Actions)
        p2ActionsJava = self.getDeque(p2Actions)
        
        frameDataAfter = self.simulator.simulate(frameDataBefore,True, p1ActionsJava, p2ActionsJava, 18)
        return frameDataAfter
