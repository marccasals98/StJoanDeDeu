#!/bin/bash
#SBATCH --output=diarization/NeMo/logs/slurm-%j.out  # Standard output and error log
#SBATCH --error=diarization/NeMo/errors/slurm-%j.err
#SBATCH --partition=veu
#SBATCH --job-name=diarization_NeMo   # Job name
#SBATCH --cpus-per-task=8                  # Run on 4 CPU
#SBATCH --mem=128G                    # Job memory request
#SBATCH --gres=gpu:4

python3 /home/usuaris/veu/marc.casals/StJoanDeDeu/diarization/NeMo/main.py