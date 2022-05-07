
class TreePolicy():

    def __init__(self) -> None:
        super().__init__()

    def getNode(self, current_node):
        
        while not current_node.isTerminalNode():
            
            #change to ShouldExpand() heuristics for expanding or not
            if not current_node.isFullyExpanded():
                return current_node.expand()
            else:
                current_node = current_node.bestChild()
        
        return current_node    