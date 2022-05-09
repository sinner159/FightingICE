from final_project_code.State import State
from final_project_code.wrappers.SimulatorWrapper import SimulatorWrapper
import numpy as np
class RolloutPolicy():

    def __init__(self, simulator: SimulatorWrapper) -> None:
        super().__init__()
        self.simulator = simulator

    def rollout(self, node):
        
        myActions = []
        oppActions = []
        
        totalFrames = 0
        actionFrameNum = 0
        while  True:
            
            possible_moves = node.state.actions.legalActions
            
            action = self.selectAction(possible_moves)
            oppAction = self.selectAction(possible_moves)
            
            actionFrameNum = self.simulator.getFrameNumber(action)
            
            if actionFrameNum + totalFrames > self.simulator.simulationFrameLimit:
                break

            totalFrames += actionFrameNum
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