from cProfile import run
from final_project_code.Config import CONFIGS, Config
from final_project_code.GameStarter import runGame
import subprocess
from final_project_code.action import ALL_QUICK_ACTIONS
from final_project_code.utils.Logger import Logger 
import os


port = 4242
cmd = f"start java -cp FightingICE.jar;./lib/lwjgl/*;./lib/natives/windows/*;./lib/*;  Main --limithp 400 400 --grey-bg --py4j --mute --fr 60 --json -r 1 --port {port}"
p = subprocess.Popen(cmd, shell=True)
logger = Logger(f"{os.getcwd()}/final_project_code/logs/")


for c in CONFIGS:
    runGame(port,c,logger)