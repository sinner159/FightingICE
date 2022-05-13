from final_project_code.State import State
from final_project_code.wrappers.SimulatorWrapper import SimulatorWrapper
import numpy as np
class RolloutPolicy():

    def __init__(self, simulator: SimulatorWrapper) -> None:
        super().__init__()
        self.simulator = simulator

    def rollout(self, node):
        
        possible_moves = node.state.actions.legalActions

        framesSinceStart = node.state.framesSinceStart
        initMyAction = self.selectAction(possible_moves)
        initOppAction = self.selectAction(possible_moves)

        myFrameNumber = self.simulator.getFrameNumber(initOppAction)
        oppFrameNumber = self.simulator.getFrameNumber(initOppAction)

        maxFR = max(myFrameNumber,oppFrameNumber)

        myActions = [initMyAction]
        oppActions = [initOppAction]
        
        totalFrames = 0
        totalFrames += maxFR
        
        while  maxFR + totalFrames  < self.simulator.simulationFrameLimit - framesSinceStart:
            
            action = self.selectAction(possible_moves)
            oppAction = self.selectAction(possible_moves)
            actionFrameNum = self.simulator.getFrameNumber(action)
            oppFrameNumber = self.simulator.getFrameNumber(oppAction)

            maxFR = max(actionFrameNum,oppFrameNumber)

            totalFrames += maxFR

            myActions.append(action)
            oppActions.append(oppAction)

        frameData = self.simulator.simulate(node.state.frameData,myActions,oppActions, totalFrames)    
        result_state = State(frameData)

        reward = result_state.gameResult(node.state)
        return reward
    


    def simulateOneMove(self, state, action):
        frameData = self.simulator.simulateOneMove(state, [action])
        return State(frameData)

    def selectAction(self, possible_moves):
         return possible_moves[np.random.randint(len(possible_moves))]  