import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset()

for _ in range(100):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    print("action i chose is: ", action)
    observation, reward, terminated, truncated, info = env.step(action)
    print("my reward is: ", reward)
    print("next state is: ", observation)

    if terminated or truncated:
        observation, info = env.reset()

env.close()