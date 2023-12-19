"""
Speaker Diarization.

This Script runs speaker diarization from the library Pyannote. 

\b
Requirements:
1. pyannote.audio version 3.1 or higher.
2. Hugging face account with huggingface token and the permission to use this script.

"""

import torch
from pyannote.audio import Pipeline
from pyannote.audio.pipelines.utils.hook import ProgressHook
import torchaudio
import sys
import argparse

def init_pipepline():
    """
    Initialize the pipeline.
    """
    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.0",
        use_auth_token="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")

    # send pipeline to GPU (when available)
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu") # device configuration
    pipeline.to(device)
    print(f"Running on the device: {device}")

    return pipeline

def run_diarization(pipeline, waveform, sample_rate):
    """ 
    Runs the diarization
    """
    # Use ProgressHook to track the progress of the pipeline.
    with ProgressHook() as hook:
            diarization, embeddings = pipeline({"waveform": waveform, "sample_rate": sample_rate}, 
                                            hook=hook, return_embeddings=True)
    return diarization, embeddings

def print_results(diarization, embeddings):
    """
    Prints the diarization results ina  displayed form, taking into account the different turns.
    """
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")

def main():

    pipleline = init_pipepline()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'audio_path',
        type=str,
        help="The path of the audio you want to diarize."
    )
    args = parser.parse_args()

    waveform, sample_rate = torchaudio.load(args.audio_path)
    
    diarization, embeddings = run_diarization(pipleline, waveform, sample_rate)

    print_results(diarization, embeddings)

if __name__=='__main__':
    sys.exit(main())