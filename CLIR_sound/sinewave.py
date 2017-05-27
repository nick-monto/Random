import numpy as np
from scipy.io import wavfile as wav


def sinewave(amp, freq, dur_sec, fs):
    A = amp
    f = freq
    t = np.linspace(0, dur_sec, np.int(fs*dur_sec))
    return A*np.sin(2*np.pi*f*t)


def audio_gen(sinewave, samp_hz, file_name):
    wav.write(file_name, samp_hz, sinewave)
    print('Saving sound file to current working directory...')
