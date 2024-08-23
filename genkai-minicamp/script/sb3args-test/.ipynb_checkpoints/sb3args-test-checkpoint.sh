#!/bin/sh
#PJM -L rscgrp=b-batch
#PJM -L gpu=1
#PJM -L elapse=0:10:00
#PJM -L jobenv=singularity
#PJM -j

module load singularity-ce
singularity exec --nv ~/genkai-test-bash.sif python3 ./sb3args-test.py 
