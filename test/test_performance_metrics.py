from final_project_code.metrics.PerformanceMetrics import PerformanceMetrics, RoundData
from final_project_code.utils.Logger import Logger
from final_project_code.Config import Config
import os


p = PerformanceMetrics(Config())
p.roundData.append(RoundData())
p.roundData.append(RoundData())
p.roundData.append(RoundData())
cwd = os.getcwd()
logger = Logger(f"{cwd}/Gym-FightingICE/final_project_code/logs/")
p.write_to_log(logger)
a=0