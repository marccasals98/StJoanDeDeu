import matplotlib.pyplot as plt 
import os
import numpy as np
import random 
import librosa, librosa.display
import seaborn as sns


def plot_waveform(audio_path: str):
    """
    Plots the waveform

    Inputs:
    -------
    audio_path: str
        The path that points to the audio that you want to plot.
    """
    print(f"The audiopath is: {audio_path}")
    sig, sr = librosa.load(audio_path)
    time = np.arange(0, len(sig)) / sr
    plt.plot(time, sig, color="lightslategray")


def diarization_plot(ref: list[tuple[str, float, float]],
                    hyp: list[tuple[str, float, float]],
                    ylim: tuple[float, float] = None,
                    audio_path:str=None):
    """
    The main function of the diarization plot.

    Inputs:
    -------
    ref: list[tuple[str, float, float]]
        The ground truth list of tuples containing (Speaker, Start, End)
    
    hyp: list[tuple[str, float, float]]
        The predictions list of tuples containing (Speaker, Start, End)
    
    ylim: tuple(ymin, ymax), Optional

    audio_path: str, Optional
        The path of the audio in order to plot it.

    """
    # Setting seaborn theme:
    sns.set_theme()

    # Initializate the matplotlib figure
    plt.figure()

    # Plotting the Waveform of the audiopath.
    if audio_path is not None:
        plot_waveform(audio_path=audio_path)
    else:
        print("If you want a plot of the waveform, please introduce its path.")

    # Setting the limits of the y-axis of the plot.
    plt.ylim(ylim[0],ylim[1])
    
    plt.title("Diarization predictions (top)  VS ground truth (bottom)")
    plt.xlabel("Time (s)")

    # To print lines depending on the speaker.
    speaker_colours = {}

    # plot the reference
    for r in ref:
        speaker = r[0]
        if speaker not in speaker_colours:
            speaker_colours[speaker] = '#' + "%06x" % random.randint(0, 0xFFFFFF)
        plt.hlines(y=-0.1, xmin=r[1], xmax=r[2],color=speaker_colours[speaker], linewidth=7.0, linestyle='-', label="Ground Truth")

    # plot the predictions 
    for h in hyp:
        speaker = h[0]
        if speaker not in speaker_colours:
            speaker_colours[speaker] = '#' + "%06x" % random.randint(0, 0xFFFFFF)
        plt.hlines(y=0.1, xmin=h[1], xmax=h[2],color=speaker_colours[speaker], linewidth=7.0, linestyle="-", label="Predictions")    

    # We will store the imatges in this path 
    imgs_path = "diarization/comparing_models/imgs"
    if not os.path.exists(imgs_path):
        os.makedirs(imgs_path)
    plt.savefig(os.path.join(imgs_path,"diarization.png"))
    