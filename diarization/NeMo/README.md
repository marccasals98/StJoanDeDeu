# NeMo

[NeMo](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/core/core.html) is a family of models designed to train and reproduce Conversational AI models:

* neural network architectures

* datasets/data loaders

* data preprocessing/postprocessing

* data augmentors

* optimizers and schedulers

* tokenizers

These models make use of [Hydra](https://hydra.cc/). Also this NeMo model is also designed to do [speaker diarization](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/speaker_diarization/intro.html). 

The pipeline follwed by NVIDIA is the following.

Audio &rarr; ASR &rarr; Speaker Diarization &rarr; Speaker Labels. 

NeMo speaker diarization system consists of the following modules:

* **Voice Activity Detector (VAD):** A trainable model which detects the presence or absence of speech to generate timestamps for speech activity from the given audio recording.

* **Speaker Embedding Extractor:** A trainable model that extracts speaker embedding vectors containing voice characteristics from raw audio signal.

* **Clustering Module:** A non-trainable module that groups speaker embedding vectors into a number of clusters.

* **Neural Diarizer:** A trainable model that estimates speaker labels from the given features.

## How to run:

To run the model at inference you need a computer with, at least, 16Gb of RAM memory. Ideally, it would be better to make use of GPU.

0. Activate the venv.

1. First of all, the model needs a .json file with some information. This file is created in the file ```manifest_creator.py```.

    'audio_filepath': "diarization/jueves_a_las_13-27.wav", 
    'offset': 0, 
    'duration':None, 
    'label': 'infer', 
    'text': '-', 
    'num_speakers': 2, 
    'rttm_filepath': None, 
    'uem_filepath' : None

```audio_filepath```: is where the wav is stored.

```num_speakers```: (default: None) is the number of speakers that the audio contains. 

```rttm_filepath```: this code performs an evaluation if a ground truth of the rttm is provided. 

2. Run the script main.py

```python3 diarization/NeMo/main.py ```