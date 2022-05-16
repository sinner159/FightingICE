from cProfile import run
from final_project_code.Chromosome import Chromosome
from final_project_code.Config import CONFIGS, Config
from final_project_code.GAActionSelection import GAActionSelection
from final_project_code.GameStarter import runGame
import subprocess
from final_project_code.action import ALL_QUICK_ACTIONS
from final_project_code.utils.Logger import Logger 
import os

port = 4242
cmd = f"start java -cp FightingICE.jar;./lib/lwjgl/*;./lib/natives/windows/*;./lib/*;  Main --limithp 1 1 --grey-bg --py4j --mute --fr 60 --json -r 1 --port {port}"
p = subprocess.Popen(cmd, shell=True)
logger = Logger(f"{os.getcwd()}/final_project_code/logs/")
c = Config()
ga = GAActionSelection("",10,8)
ga.initialization()
ga.population
chrm: Chromosome


for chrm in ga.population:
    c.action_set = chrm.actions
    c.action_set_name = chrm.name

    pm = runGame(port,c,logger)
    chrm.performanceMetrics = pm

newPop = ga.selection()
ga.recombination(newPop)
ga.mutation()


a=0
