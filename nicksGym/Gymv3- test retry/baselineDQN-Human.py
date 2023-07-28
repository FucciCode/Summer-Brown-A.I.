import gymnasium as gym
#import gym
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
import random

env_id = "ALE/Tetris-ram-v5"
num_env = 8
seed = random.randint(0, 2**31)
env = make_vec_env(env_id, n_envs=num_env, seed=seed)
obs_type = "ram"

try:
    print("Trying to load model...")
    model = DQN.load("dqn_tetris_model", env=env, learning_rate=.1)
    print("Model loaded.")
except ValueError:
    buffer_size = 10000  # reduce from 1 million to 10 thousand
    model = DQN("MlpPolicy", env, buffer_size=buffer_size, verbose=1,)
    print("No model found, starting from scratch.")

obs = env.reset()
print("while loop starting")
while True:
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = env.step(action)
    env.render("human")
    if any(dones):
        obs = env.reset()

