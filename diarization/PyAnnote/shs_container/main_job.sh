#!/bin/bash
#SBATCH --output=diarization/PyAnnote/logs/slurm-%j.out  # Standard output and error log
#SBATCH --error=diarization/PyAnnote/errors/slurm-%j.err
#SBATCH --partition=gpi.compute11
#SBATCH --job-name=diarization_pyannote    # Job name
#SBATCH --cpus-per-task=4                  # Run on 4 CPU
#SBATCH --mem=64G                    # Job memory request
#SBATCH --gres=gpu:4

python diarization/PyAnnote/diarization_test.py