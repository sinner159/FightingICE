from argparse import Action


class GatewayWrapper():

    def __init__(self, gateway):
        self.gateway = gateway

    def getDeque(self, objects):
        deque = self.gateway.jvm.java.util.LinkedList()
        
        for obj in objects:
            enum = self.gateway.jvm.enumerate.Action.valueOf(obj)
            deque.add(enum)
        
        return deque