# Diarization

We are doing speaker diarization making use of three techniques. The audio that is used for testing is ```jueves_a_las_13-27.wav```, it has its version in a m4a. 

The task description is a .json file generated after making the labeling with Label Studio.

## Pyannote

This is the by-default technique of the project. It is done in ```diarization_test.py```.

## NeMo

NeMo is the approach of NVIDIA. To use it just go to the folder NeMo that contains all of the information. 

## WhisperX

WhisperX do ASR and Speaker diarization at the same time. 


## Results:

The results obtained are:

|          	| DER  (Light)     	        | DER (Simplified)  | DER (Pyannote metric) 
|----------	|-------	                | -------           | -------
| Pyannote 	| 0.168 	                | 0.17028           | 0.17263
| WhisperX 	| 0.221 	                | 0.21672           | 0.21859
| NeMo     	| None  	                | None              | None

The different metrics that are in the table are:
1. DER (Light): DER without overlapping (manually modifying) using the following [GitHub](https://github.com/wq2012/SimpleDER)
2. DER (Simplified): DER without overlapping using Pyannote library.
3. DER (Pyannote metric): DER with overlapping using Pyannote Library.


### Collar modifications

The goal now is to track the different DERs that are obtained when modifying the collar parameter. In order to do this, we are only going to consider the Pyannote with Pyannote metric.

| Collar 	| 0       	| 0.5     	| 1       	| 2        	| 5       	| 10      	|
|--------	|---------	|---------	|---------	|----------	|---------	|---------	|
| DER    	| 0.17264 	| 0.11631 	| 0.10058 	| 0.101501 	| 0.12321 	| 0.15093 	|

## Plot Diarization
There is a script that is dedicated to plotting the Diarization. Here we have an example with the audio file of St. Joan de Déu:

![image](https://github.com/marccasals98/StJoanDeDeu/assets/97680577/0e6a7c21-466b-49fd-b5f7-d711772800bd)
