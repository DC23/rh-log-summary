#!/bin/bash -login
#SBATCH --job-name=scratch2-purge-dry-run-summariser
#SBATCH --account=astronomy856
#SBATCH --partition=workq
#SBATCH --nodes=1
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4

aprun -n 1 ./batch_report.sh
