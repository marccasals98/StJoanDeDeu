# st_joan

This project is mainly focused in speaker diarization and speech-to-text.

## Python environment 

To run this project it is recommended to use a Python environment. To do so:

1. Create the virtual environment:

```
python3 -m venv /path/to/new/virtual/environment
```

2. Activate the virtual environment:
```
source <venv>/bin/activate
```

3. Deactivate the virtual environment:
```
deactivate
```

Installing the requirements it is necessary to previously install [Cython](https://pypi.org/project/Cython/) by just doing ```pip install Cython```. Once it is installed, the requirements can be installed normally using the command:

```bash
pip install -r requirements.txt
```
Notice that the Cython requirement appears also in the requirements.txt. However, there is some kind of problem from which Cython is not installed firstly, which produces some error when trying to install other libraries.

## Speaker diarization

Speaker diarization is the process of automatically identifying and segmenting an audio recording into distinct speech segments, where each segment corresponds to a particular speaker.

In order to do speaker diarization we will mainly make use of the library pyannote. However, we will also compare the performance with other libraries like NeMo.

$$\text{DER}=\frac{\text{false alarm}+\text{missed detection}+\text{confussion}}{\text{total}}$$

### Diarization Error Rate (DER)

The main metric used in diarization is the DER. It is measured as the fraction of time that is not attributed correctly to a speaker or to non-speech.

## Speech-to-text

Speech-to-text is a technology that enables human speech to be converted automatically into text.

In order to do speech-to-text tasks, they will make usage of the Whisper model.

This file is just created to do an evaluation of the whisper performance. To do so, we will use the WER metric. 

### Word Error Rate (WER)    
The Word Error Rate is a common metric of the performance of a speech recognition task. 

This metric is derived from the Levenshtein distance.

To have a full comprehension of this metric let's define the following variables.

* **S:** is the number of substitutions,
* **D:** is the number of deletions,
* **I:** is the number of insertions,
* **C:** is the number of correct words,
* **N:** is the number of words in the reference (N=S+D+C)

From this, we can finally calculate this metric.

$$WER=\frac{S+D+I}{N}=\frac{S+D+I}{S+D+C}$$

From this metric we can define the Word Accuracy (WAcc) that is exaclty the complementary of this metric. 

**Example:**

*Reference text:* "The cat is sleeping on the mat."

*Recognized text:* "The cat is playing on mat."
