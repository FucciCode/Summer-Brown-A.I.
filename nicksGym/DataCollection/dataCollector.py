import gymnasium as gym

import random


env = gym.make("ALE/Tetris-ram-v5", render_mode="human")

obs, info  = env.reset()
print("while loop starting")
while True:
    print("these are the available actions:")
    # print(env.action_space)

    # action, _states =
    # obs, rewards, dones, info = env.step(action)
    env.render()
    # if any(dones):
    #     obs = env.reset()

