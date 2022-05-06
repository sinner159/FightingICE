from final_project_code.wrappers.GatewayWrapper import GatewayWrapper


class SimulatorAdapter(GatewayWrapper):

    def __init__(self, gateway, simulator):
        super().__init__(gateway)
        self.simulator = simulator

#simulate(FrameData frameData, 
# boolean playerNumber, 
# java.util.Deque<Action> myAct, 
# java.util.Deque<Action> oppAct, 
# int simulationLimit)
    def simulateMove(self,p1Actions, p2Actions):
        p1ActionsJava = self.getDeque(p1Actions)
        p2ActionsJava = self.getDeque(p2Actions)
        
        frameData = self.simulator.simulate(self.frameData,True, p1ActionsJava, p2ActionsJava, 1)
        return frameData
