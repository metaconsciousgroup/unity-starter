import numpy as np
from mlagents_envs.environment import UnityEnvironment
from mlagents_envs.envs.unity_gym_env import UnityToGymWrapper

# Location of the Unity binary
FILENAME = "./unity/CareBot3D/carebot3d.app"

# Build env and convert to Gym env
unity_env = UnityEnvironment(file_name=FILENAME, seed=1, side_channels=[])
env = UnityToGymWrapper(unity_env)

# Start interacting with the environment
obs = env.reset()
for i in range(1000):
    action = env.action_space.sample()
    # action = np.array([0, 0, 1, 0])
    # action = brain(obs)
    obs, reward, done, info = env.step(action)
    print(i)
    if reward > 0:
        print(obs.shape, reward, done, info)

