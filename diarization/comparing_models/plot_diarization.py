import matplotlib.pyplot as plt 
import os
import wave 
import numpy as np
import random 
import librosa, librosa.display
import seaborn as sns


def plot_waveform(audio_path):
    """
    Plots the waveform
    """
    sig, sr = librosa.load(audio_path)
    time = np.arange(0, len(sig)) / sr
    # sig = np.frombuffer(sig.readframes(sr), dtype=np.int16)
    plt.plot(time, sig, color="lightslategray")
    plt.ylim(-0.4,0.3)



def diarization_plot(ref: list[tuple[str, float, float]], hyp: list[tuple[str, float, float]], audio_path:str=None):
    """
    The main function of the diarization plot.

    Inputs:
    -------
    ref: list[tuple[str, float, float]]
        The ground truth list of tuples containing (Speaker, Start, End)
    
    hyp: list[tuple[str, float, float]]
        The predictions list of tuples containing (Speaker, Start, End)

    audio_path: str
        The path of the audio in order to plot it.

    """

    if audio_path is None:
        audio_path = "diarization/jueves_a_las_13-27.wav"

    sns.set_theme()

    plt.figure()

    plot_waveform(audio_path=audio_path)

    # To print lines depending on the speaker.
    speaker_colours = {}

    # plot the reference
    for r in ref:
        speaker = r[0]

        if speaker not in speaker_colours:
            speaker_colours[speaker] = '#' + "%06x" % random.randint(0, 0xFFFFFF)

        plt.hlines(y=-0.1, xmin=r[1], xmax=r[2],color=speaker_colours[speaker], linestyle='-')

    # plot the predictions 
    for h in hyp:
        speaker = h[0]

        if speaker not in speaker_colours:
            speaker_colours[speaker] = '#' + "%06x" % random.randint(0, 0xFFFFFF)

        plt.hlines(y=0.1, xmin=h[1], xmax=h[2],color=speaker_colours[speaker], linestyle="dotted")    

    # We will store the imatges in this path 
    imgs_path = "diarization/comparing_models/imgs"
    if not os.path.exists(imgs_path):
        os.makedirs(imgs_path)
    plt.savefig(os.path.join(imgs_path,"diarization.png"))
    