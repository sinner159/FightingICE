import gym
import gym_fightingice
import random
from threading import Thread
from gym_fightingice.envs.Machete import Machete
from gym_fightingice.envs.fightingice_env_twoplayer import play_thread
import time
import os
from gym_fightingice.envs.gym_ai import GymAI
from gym_fightingice.testAI import TestAI

def p_thread1(env,p1,p2):
    while True:
        obs = env.reset(p1=p1,p2=p2)

        done = False
        while not done:
            new_obs, reward, done, _ = env.step(22)

def p_thread2(env,p1,p2):
    while True:
        obs = env.reset(p1=p1,p2=p2)

        done = False
        while not done:
            new_obs, reward, done, _ = env.step(38)

cwd = f"{os.getcwd()}"
env1 = gym.make("FightingiceDataTwoPlayer-v0", java_env_path=cwd,port=4242, freq_restart_java=3)
p2_server = env1.build_pipe_and_return_p2()
env2 = gym.make("FightingiceDataTwoPlayer-v0", java_env_path=cwd,port=4242,p2_server=p2_server)
t1 = Thread(target=p_thread1, name="play_thread1", args=(env1,TestAI,GymAI, ))
t2 = Thread(target=p_thread2, name="play_thread2", args=(env2,TestAI,GymAI, ))
t1.start()
time.sleep(10)
t2.start()
while True:
    t1.join()
    t2.join()

print("finish")
