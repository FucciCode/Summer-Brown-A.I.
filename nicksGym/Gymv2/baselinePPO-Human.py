import gymnasium as gym
#import gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
import random

env_id = "ALE/Tetris-ram-v5"
num_env = 8
seed = random.randint(0, 2**31)
env = make_vec_env(env_id, n_envs=num_env, seed=seed)
obs_type = "ram"

learning_rate = 0.5  # You can adjust this value as needed

try:
    print("Trying to load model...")
    model = PPO.load("ppo_tetris_model", env=env, learning_rate=learning_rate)
    print("Model loaded.")
except ValueError:
    model = PPO("MlpPolicy", env, learning_rate=learning_rate, verbose=1)
    print("No model found, starting from scratch.")

obs = env.reset()
print("while loop starting")
while True:
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = env.step(action)
    env.render("human")
    if any(dones):
        obs = env.reset()

