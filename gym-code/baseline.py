import gym 
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
import random

# Parallel environments
seed = random.randint(0, 2**31)
env_name = "ALE/Tetris-ram-v5" #Ram 
vec_env = make_vec_env(env_name, n_envs=16, seed = 12345)

obs_type = "ram"


print("Model does not exist.")
model = A2C("MlpPolicy", vec_env, verbose=1)




model.set_env(vec_env)
model.learn(total_timesteps=1000000)
model.save("a2c_tetris_model")

