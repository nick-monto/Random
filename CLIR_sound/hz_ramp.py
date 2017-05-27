from sinewave import sinewave, audio_gen
import numpy as np
from scipy.io import wavfile as wav

wave = sinewave(2, 220, 0.25, 44100)

div_list = []

a = 2
while a >= 0.000001:
    div_list.append(a)
    a = a - (1/20*a)

fz_ramp = wave

for i in div_list:
    fz_ramp = np.append(fz_ramp,
                        np.zeros(len(np.linspace(0, i, np.int(i*44100)))))
    fz_ramp = np.append(fz_ramp, wave)


audio_gen(fz_ramp, 44100, './working.wav')
