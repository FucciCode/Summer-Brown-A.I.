import gym
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
import random

seed = random.randint(0, 2**31)
env_name = "ALE/Tetris-ram-v5" 
vec_env = make_vec_env(env_name, n_envs=16, seed = 12345)

obs_type = "ram"

try:
     model = A2C.load("a2c_tetris_model")

except ValueError:
     #If no pretrained model is found, create a new model
     print("Model does not exist.")
     model = A2C("MlpPolicy", vec_env, verbose=1)



obs = vec_env.reset()

while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = vec_env.step(action)
    print(obs.shape)
    vec_env.render("human")