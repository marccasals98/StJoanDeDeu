#!/bin/bash
#SBATCH --output=diarization/comparing_models/logs/slurm-%j.out  # Standard output and error log
#SBATCH --error=diarization/comparing_models/errors/slurm-%j.err
#SBATCH --partition=veu
#SBATCH --job-name=diarization_pyannote    # Job name
#SBATCH --cpus-per-task=8                  # Run on 4 CPU
#SBATCH --mem=256G                    # Job memory request
#SBATCH --gres=gpu:0

python3 diarization/comparing_models/abir_method.py\
