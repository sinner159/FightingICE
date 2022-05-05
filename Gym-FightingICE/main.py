import gym
import sys, os

sys.path.append('gym-fightingice')
from gym_fightingice.envs.Machete import Machete

def main():
    env = gym.make("FightingiceDataNoFrameskip-v0", java_env_path=os.getcwd(), port=4242)
    env.reset(p2=Machete)
    
    for i in range(300):
        env.step(0)




if __name__ == "__main__":
    main()
