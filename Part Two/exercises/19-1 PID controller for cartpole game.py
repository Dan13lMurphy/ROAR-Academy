import gym
import numpy as np
import time

Kp = 1.0
Ki = 0.01
Kd = 0.5

integral = 0
previous_error = 0

env = gym.make('CartPole-v1')

for episode in range(5):
    obs = env.reset()
    if isinstance(obs, tuple):
        obs = obs[0]

    total_reward = 0
    integral = 0
    previous_error = 0

    for t in range(500):
        env.render()

        pole_angle = obs[2]
        error = pole_angle

        integral += error
        derivative = error - previous_error
        control = Kp * error + Ki * integral + Kd * derivative

        action = 1 if control > 0 else 0

        result = env.step(action)
        if isinstance(result, tuple):
            obs, reward, done, truncated, info = result
        else:
            obs, rewards, done, info = result
            truncated = False
        total_reward += reward
        previous_error = error

        if done or truncated:
            break
    print(f"Episode {episode+1} finished with reward: {total_reward}")

env.close()
