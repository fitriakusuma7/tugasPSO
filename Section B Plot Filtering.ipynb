import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

np.random.seed(0)
t = np.linspace(0, 1, 1000, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t)
noise = 0.5 * np.random.normal(size=t.shape)
noisy_signal = signal + noise

fs = 1000
cutoff_freq = 10
order = 4

def butter_lowpass(cutoff, fs, order=4):
    nyquist_freq = 0.5 * fs
    normal_cutoff = cutoff / nyquist_freq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=4):
    b, a = butter_lowpass(cutoff, fs, order=order)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

filtered_signal = butter_lowpass_filter(noisy_signal, cutoff_freq, fs, order)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, noisy_signal)
plt.title('Original Noisy Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal, color='green')
plt.title('Filtered Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

#Printing ID
print("Nama: Fitria Kusumaningrum")
print("NRP: 5009201044")