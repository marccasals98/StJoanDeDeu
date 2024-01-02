# PyAnnote

To use PyAnnote it is necessary to have a huggingface token with access to PyAnnote.

# Getting Started.

There are two ways of running this script.

1. Directly by running with Python using the commmand:
```bash
python3 diarization/PyAnnote/diarization_test.py filepath
```

2. Or, if the cluster has SLURM installed, by using:
```bash
sbatch diarization/PyAnnote/shs_container/main_job.sh 
```
Make sure to provide in the ```main_job.sh`` the proper slurm configurations and the proper audio path as well. 


## Files:

1. ```parlament_predicts.txt```: PyAnnote predictions of the first audiofile.
2. ```parlament_predicts2.txt```: PyAnnote predictions of the second audiofile.
3. ```results.txt```: Is the ground truth.    
4. ```results.txt```: Is the ground truth without overlapping.
    