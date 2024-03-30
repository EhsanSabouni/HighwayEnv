import gymnasium as gym

env = gym.make('highway-v0', render_mode='human')

obs, info = env.reset()
done = truncated = False
while not (done or truncated):
    action = 0
    obs, reward, done, truncated, info = env.step(action)
    print(obs,reward, done, info)