# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr

data_dir = '/home/mithradiel/Downloads/Musics/Slipknot/'
audio_file = glob(data_dir + '/snuff.wav')
audio, sfreq = lr.load(audio_file[0])
time = np.arange(0, len(audio)) / sfreq

D_left = np.abs(lr.stft(audio, center=False))
print(len(D_left[0]))
print(len(audio))

fig, (ax, ax2) = plt.subplots(2)
ax.plot(time, audio)

ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
print("Mostrar")
plt.show()