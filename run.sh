#!/bin/sh
#SBATCH --job-name=Dry-run Purge log summariser
#SBATCH --account=
#SBATCH --partition=
#SBATCH --nodes=1
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1

module load python

LOG_FILE=/scratch2/PurgeTest
MAX_RECORDS=10000

aprun -n 1 \
python ./rbh_log_summary.py \
--atime_threshold 30.0 \
--max_records $MAX_RECORDS \
$LOG_FILE
