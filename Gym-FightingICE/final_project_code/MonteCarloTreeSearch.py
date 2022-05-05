from final_project_code.Node import Node


class MonteCarloTreeSearch():
    
    def select(self) -> Node:
        raise NotImplementedError

    def expand(self) -> Node:
        raise NotImplementedError

    def simulate(self) -> float:
        raise NotImplementedError

    def back_propogate(self):
        raise NotImplementedError
    
    def search(self) -> str:
        raise NotImplementedError