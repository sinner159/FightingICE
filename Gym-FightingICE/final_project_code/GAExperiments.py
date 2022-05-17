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
generation_count = 10
loadFromFile = True
c = Config(maxHP=100,rounds=1)
cmd = f"start java -cp FightingICE.jar;./lib/lwjgl/*;./lib/natives/windows/*;./lib/*;  Main --limithp {c.maxHP} {c.maxHP} --grey-bg --py4j --mute --fr 60 --json -r {c.rounds} --port {port}"
dir = f"{os.getcwd()}/final_project_code"
p = subprocess.Popen(cmd, shell=True)
logger = Logger(f"{dir}/logs/")

#                       populationSize, chromosomeLength, selection_size, logger
ga = GAActionSelection(f"{dir}/generation/Generation.txt",populationSize=6,chromosomeLength=10,selection_size=6,logger=logger)
if loadFromFile:
    ga.loadFromFile()
else:
    ga.initialization()

for i in range(generation_count):
    chrm: Chromosome
    logger.write(f"Running simulations for Generation {i}")
    logger.write(f"Population of Gen {i}")
    logger.write(ga.populationAsString())
    for chrm in ga.population:
        logger.write(F"Simulating for {chrm.name}")
        c.action_set = chrm.actions
        c.action_set_name = chrm.name
        try:
            pm = runGame(port,c,logger)
        except Exception as ex:
            print("Error running runGame: " + ex)
            os.wait(1000)
            print("Trying again")
            pm = runGame(port,c,logger)

        chrm.performanceMetrics = pm
        pm.write_to_log(logger)

    newPop = ga.selection()
    ga.recombination(newPop)
    ga.mutation()



