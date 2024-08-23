import argparse
#Default args
exp_no = 0
ALGO = "PPO"
env_id = "BreakoutNoFrameskip-v4"
SEED = 0
NUM_ENVS = 32
TRAIN_STEPS = 1E4
N_EVAL_EPISODES = 100

import os
import sys
import git
import pathlib

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

PROJ_ROOT_PATH = pathlib.Path(git.Repo('.', search_parent_directories=True).working_tree_dir)
PROJ_ROOT =  str(PROJ_ROOT_PATH)
if PROJ_ROOT not in sys.path:
    sys.path.append(PROJ_ROOT)

print(f"Project Root Directory: {PROJ_ROOT}")

import numpy as np
import matplotlib.pyplot as plt

import gymnasium as gym
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3 import PPO, A2C, DQN
from stable_baselines3.common.results_plotter import load_results, ts2xy
from stable_baselines3.common.evaluation import evaluate_policy

exp_tag = "vanilla"
exp_name = f"{env_id}--{ALGO}--{exp_tag}"

# # Parse Arguments
# parser = argparse.ArgumentParser()
# parser.add_argument('exp_no')
# parser.add_argument('ALGO')
# parser.add_argument('env_id')
# parser.add_argument('SEED')
# parser.add_argument('NUM_ENVS')
# parser.add_argument('TRAIN_STEPS')
# parser.add_argument('N_EVAL_EPISODES')

# args= parser.parse_args()

# exp_no = args.exp_no
# ALGO = args.ALGO
# env_id = args.env_id
# SEED = args.SEED
# NUM_ENVS = args.NUM_ENVS
# TRAIN_STEPS = args.TRAIN_STEPS
# N_EVAL_EPISODES = args.N_EVAL_EPISODES

logfolder_root = pathlib.Path(PROJ_ROOT_PATH / "sb3" / "notebook" / "logging")

# Directory to save all training statistics
log_dir = pathlib.Path(logfolder_root / exp_name)
os.makedirs(log_dir, exist_ok=True)

# Directory to save gif animations
gif_dir = pathlib.Path(log_dir / "gifs" / exp_name)
os.makedirs(gif_dir, exist_ok=True)

# Directory to save models
models_dir = pathlib.Path(PROJ_ROOT_PATH / "models" / exp_name)
os.makedirs(models_dir, exist_ok=True)

for experiment in [exp_no]:
    print("-------")
    print(f"RUN: {experiment}")
    # Log directory for each run of the experiment
    run_log_dir = f"{log_dir}/run_{experiment}"
    
    # Make vector environment
    env = make_atari_env(env_id,
                         n_envs=NUM_ENVS,
                         monitor_dir=run_log_dir,
                         seed=SEED+experiment)
    
    # Frame-stacking with 4 frames
    env = VecFrameStack(env, n_stack=4)

    # Create RL model
    model = eval(ALGO)("CnnPolicy", env, verbose=0)

    # Train the agent
    model.learn(total_timesteps=TRAIN_STEPS)

    # Save the final agent
    model.save(f"{models_dir}/{exp_name}-run_{experiment}")

# Evaluate Model

trained_model = eval(ALGO).load(f"{models_dir}/{exp_name}-run_{experiment}", verbose=1)
eval_env = make_atari_env(env_id,
                         n_envs=NUM_ENVS, 
                          seed=SEED+experiment+7)
eval_env = VecFrameStack(eval_env, n_stack=4)
trained_model.set_env(eval_env)

mean_rew, mean_std=evaluate_policy(trained_model,
                                   trained_model.env, 
                                   n_eval_episodes=N_EVAL_EPISODES)
								   
print(f" Avg Reward: {mean_rew:.2f} \u00B1 {mean_std:.2f}")