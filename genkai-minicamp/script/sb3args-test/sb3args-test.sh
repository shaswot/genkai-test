#!/bin/sh
#PJM -L rscgrp=b-batch
#PJM -L gpu=1
#PJM -L elapse=0:10:00
#PJM -L jobenv=singularity
#PJM -j

module load singularity-ce
singularity exec --nv ~/genkai-test-bash.sif python3 ./sb3args-test.py --exp_no=5 --ALGO=PPO 


#python3 ./sb3args-test.py --exp_no=0 \
#                            --ALGO=A2C \
#                            --env_id=BreakoutNoFrameskip-v4 \
#                            --SEED=0 \
#                            --NUM_ENVS=16\
#                            --TRAIN_STEPS=10_000\
#                            --N_EVAL_EPISODES=100
