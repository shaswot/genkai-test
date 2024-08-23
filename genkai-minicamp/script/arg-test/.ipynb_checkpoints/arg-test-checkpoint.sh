#!/bin/sh
JOBNAME="arg-test"
#PJM -L rscgrp=b-batch
#PJM -L gpu=1
#PJM -L elapse=0:10:00
#PJM -L jobenv=singularity
#PJM -N $JOBNAME
#PJM -o $JOBNAME.out
#PJM -e $JOBNAME.err

module load singularity-ce
singularity exec --nv ~/genkai-test-bash.sif python3 ./arg-test.py 
