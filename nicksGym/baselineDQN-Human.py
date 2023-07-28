import gymnasium as gym
#import gym
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
import random

num_envs = 8
seed = random.randint(0, 2**31)
env = gym.make("ALE/Tetris-ram-v5", render_mode="human", seed = 12345) #, seed=seed)


try:
    print("Trying to load model...")
    model = DQN.load("dqn_tetris_model")
    print("Model loaded.")
except ValueError:
    buffer_size = 10000  # reduce from 1 million to 10 thousand
    model = DQN("MlpPolicy", env, buffer_size=buffer_size, verbose=1,)
    print("No model found, starting from scratch.")

obs, info = env.reset()

print("while loop starting")
while True:
    action, states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, info = env.reset()

