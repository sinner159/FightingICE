from uuid import uuid1


class Chromosome():

    def __init__(self):
        self.actions: list = []
        self.performanceMetrics = None
        self.name = str(uuid1())

    def addAction(self, action: list):
        self.actions.append(action)


    def __str__(self):
        return ''.join(self.actions)
    
    def __repr__(self) -> str:
        return str(self)
    