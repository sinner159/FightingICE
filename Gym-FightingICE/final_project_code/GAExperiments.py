from cProfile import run
from operator import ge
from final_project_code.Chromosome import Chromosome
from final_project_code.Config import CONFIGS, Config
from final_project_code.GAActionSelection import GAActionSelection
from final_project_code.GameStarter import runGame
import subprocess
from final_project_code.action import ALL_QUICK_ACTIONS
from final_project_code.utils.Logger import Logger 
import os

port = 4242
generation_count = 3
cmd = f"start java -cp FightingICE.jar;./lib/lwjgl/*;./lib/natives/windows/*;./lib/*;  Main --limithp 20 20 --grey-bg --py4j --mute --fr 60 --json -r 1 --port {port}"
p = subprocess.Popen(cmd, shell=True)
logger = Logger(f"{os.getcwd()}/final_project_code/logs/")
c = Config()
ga = GAActionSelection("",6,8)
ga.initialization()

for i in range(generation_count):
    chrm: Chromosome
    logger.write(f"Running simulations for Generation {generation_count}")
    for chrm in ga.population:
        c.action_set = chrm.actions
        c.action_set_name = chrm.name
        print(chrm)
        pm = runGame(port,c,logger)
        chrm.performanceMetrics = pm

    newPop = ga.selection()
    ga.recombination(newPop)
    ga.mutation()



