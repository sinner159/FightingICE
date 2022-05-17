import sys
from time import sleep
from final_project_code.Config import Config
from final_project_code.PerformanceMetrics import PerformanceMetrics
from final_project_code.utils.Logger import Logger
from gym_fightingice.envs.Machete import Machete
from python.KickAI import KickAI
from final_project_code.TestAI import TestAI
from python.DisplayInfo import DisplayInfo
from py4j.java_gateway import JavaGateway, GatewayParameters, CallbackServerParameters, get_field
import subprocess 

port = 4242
cmd = f"start java -cp FightingICE.jar;./lib/lwjgl/*;./lib/natives/windows/*;./lib/*;  Main --limithp 400 400 --grey-bg --py4j --mute --fr 60 --json -r 1 --port {port}"
p = subprocess.Popen(cmd,shell=True)

gateway = JavaGateway(gateway_parameters=GatewayParameters(port=port,auto_field=True), callback_server_parameters=CallbackServerParameters());
manager = gateway.entry_point

p1 = TestAI(gateway, Config())

manager.registerAI(p1.__class__.__name__, p1)
print("Start game")

game = manager.createGame("ZEN", "ZEN", p1.__class__.__name__, "Toothless", 1)
manager.runGame(game)

print("After game")

sys.stdout.flush()


gateway.close_callback_server()
gateway.close()
p.kill()
