import sys
from final_project_code.Config import Config
from final_project_code.TestAI import TestAI
from py4j.java_gateway import JavaGateway, GatewayParameters, CallbackServerParameters

def runGame(port, config :Config, logger):
   
    gateway = JavaGateway(gateway_parameters=GatewayParameters(port=port,auto_field=True), callback_server_parameters=CallbackServerParameters());
    manager = gateway.entry_point

    p1 = TestAI(gateway, config, logger)

    manager.registerAI(p1.__class__.__name__, p1)
    print("Start game")

    game = manager.createGame("ZEN", "ZEN", p1.__class__.__name__, config.opp_ai, 1)
    manager.runGame(game)

    print("After game")

    sys.stdout.flush()

    gateway.close_callback_server()
    gateway.close()

    return p1.performanceMetrics
