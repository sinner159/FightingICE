import numpy as np
class RolloutPolicy():

    def __init__(self) -> None:
        super().__init__()

    def getNode(self, possible_moves):
         return possible_moves[np.random.randint(len(possible_moves))]  