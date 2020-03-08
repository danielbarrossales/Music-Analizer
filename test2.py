# -*- coding: utf-8 -*-
import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr

data_dir = '/home/mithradiel/Downloads/Musics/Slipknot/'
audio_file = glob(data_dir + '/snuff.wav')

audio, sfreq = lr.load(audio_file[0])
time = np.arange(0, len(audio)) / sfreq

fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
plt.show()


