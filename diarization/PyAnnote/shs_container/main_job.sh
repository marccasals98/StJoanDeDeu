#!/bin/bash
#SBATCH --output=diarization/PyAnnote/logs/slurm-%j.out  # Standard output and error log
#SBATCH --error=diarization/PyAnnote/errors/slurm-%j.err
#SBATCH --partition=veu
#SBATCH --job-name=diarization_pyannote    # Job name
#SBATCH --cpus-per-task=4                  # Run on 4 CPU
#SBATCH --mem=128G                    # Job memory request
#SBATCH --gres=gpu:4

python3 diarization/PyAnnote/diarization_test.py\
	'/home/usuaris/veu/marc.casals/943684.wav'
