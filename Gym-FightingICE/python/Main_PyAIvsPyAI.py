import sys
from time import sleep
from final_project_code.PerformanceMetrics import PerformanceMetrics
from final_project_code.utils.Logger import Logger
from python.KickAI import KickAI
from final_project_code.TestAI import TestAI
from python.DisplayInfo import DisplayInfo
from py4j.java_gateway import JavaGateway, GatewayParameters, CallbackServerParameters, get_field
import os

def check_args(args):
	for i in range(argc):
		if args[i] == "-n" or args[i] == "--n" or args[i] == "--number":
			global GAME_NUM
			GAME_NUM = int(args[i+1])

def start_game():
        p1 = TestAI(gateway)
        p2 = KickAI(gateway)
        
        manager.registerAI(p1.__class__.__name__, p1)
        manager.registerAI(p2.__class__.__name__, p2)
        print("Start game")
        game = manager.createGame("ZEN", "ZEN",
                                  p1.__class__.__name__,
                                  p2.__class__.__name__,
                                  GAME_NUM)
        manager.runGame(game)

        print("After game")
        sys.stdout.flush()

def close_gateway():
	gateway.close_callback_server()
	gateway.close()

def main_process():
	check_args(args)
	start_game()
	close_gateway()

args = sys.argv
argc = len(args)
GAME_NUM = 2
gateway = JavaGateway(gateway_parameters=GatewayParameters(port=4242, auto_field=True), callback_server_parameters=CallbackServerParameters());
manager = gateway.entry_point

main_process()

