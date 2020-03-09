# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr
import librosa.display

DB_MIN = 0
DB_MAX = 80


data_dir = '/home/mithradiel/Downloads/Musics/Slipknot/'
audio_file = glob(data_dir + '/snuff.wav')
audio, sfreq = lr.load(audio_file[0])
time = np.arange(0, len(audio)) / sfreq

D_left = np.abs(lr.stft(audio, center=False))

librosa.display.specshow(lr.amplitude_to_db(D_left,ref=np.max), y_axis='log', x_axis='time')
plt.title('Power Spectrogram')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()

fig, ax = plt.subplots()
ax.plot(time, audio)

ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
plt.show()