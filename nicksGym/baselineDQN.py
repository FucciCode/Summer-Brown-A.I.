import gymnasium as gym
#import gym
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
import random


seed = random.randint(0, 2**31)
env = make_vec_env("ALE/Tetris-ram-v5", seed=12345)

try:
    print("Trying to load model...")
    model = DQN.load("dqn_tetris_model")
    print("Model loaded.")
except ValueError:
    # buffer_size = 10000  # reduce from 1 million to 10 thousand
    # model = DQN("MlpPolicy", env, buffer_size=buffer_size, verbose=1,)
    # print("No model found, starting from scratch.")
    print("____________________ERROR FILE NOT LOADING________________________")
    exit()

print("setting env")
model.set_env(env)
print("learning......")
model.learn(total_timesteps=1000000, log_interval=10)
print("saving model")
model.save("dqn_tetris_model")
print("Model saved.")