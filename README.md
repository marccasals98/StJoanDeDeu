# st_joan

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

Installing the requirements it is necessary to previously install ```Cython``` by just doing ```pip install Cython```. Once it is installed, tje requirements can be installed normally using the command:

```bash
pip install -r requirements.txt
```

## Speaker diarization

In order to do speaker diarization we will make use of the library pyannote.

## Speech-to-text

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
