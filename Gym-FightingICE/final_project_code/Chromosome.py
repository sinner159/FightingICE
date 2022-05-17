from uuid import  uuid4


class Chromosome():

    def __init__(self):
        self.actions: list = []
        self.performanceMetrics = None
        self.name = str(uuid4())
        self.fitness = 0

    def addAction(self, action):
        self.actions.append(action)

    def addActions(self, actions: list):
        self.actions = actions.copy()
        
    def __str__(self):
        return f"ID: {self.name} actions: " + ','.join(self.actions)
    
    def __repr__(self) -> str:
        return str(self)
    