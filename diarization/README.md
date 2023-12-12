# Diarization

We are doing speaker diarization making use of three techniques. The audio that is used for testing is ```jueves_a_las_13-27.wav```, it has its version in a m4a. 

The task description is a .json file generated after making the labeling with Label Studio.

## Pyannote

This is the by-default technique of the project. It is done in ```diarization_test.py```

## NeMo

NeMo is the approach of NVIDIA. To use it just go to the folder NeMo that contains all of the information. 

## WhisperX

WhisperX do ASR and Speaker diarization at the same time. 


## Results:

The results obtained are:

|          	| DER   	|
|----------	|-------	|
| Pyannote 	| 0.168 	|
| WhisperX 	| 0.221 	|
| NeMo     	| None  	|

As we can see the best results are obtained with Pyannote. At the moment NeMo is not working. 