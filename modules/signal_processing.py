import numpy as np
from scipy.signal import butter, filtfilt


# bandpass filter
def bandpass_filter(signal, low=0.7, high=4.0, fs=30):

    if len(signal) < 30:
        return signal

    nyquist = 0.5 * fs

    low /= nyquist
    high /= nyquist

    b, a = butter(2, [low, high], btype="band")

    filtered = filtfilt(b, a, signal)

    return filtered


# breathing filter
def respiration_filter(signal, low=0.1, high=0.5, fs=30):

    if len(signal) < 30:
        return signal

    nyquist = 0.5 * fs

    low /= nyquist
    high /= nyquist

    b, a = butter(2, [low, high], btype="band")

    filtered = filtfilt(b, a, signal)

    return filtered


# compute heart rate & respiration
def process_signal(signal_buffer, fps=30):

    signal = np.array(signal_buffer)

    if len(signal) < 30:
        return 0, 0, signal

    # normalize
    signal = signal - np.mean(signal)

    # filter heart signal
    heart_signal = bandpass_filter(signal)

    # filter respiration signal
    resp_signal = respiration_filter(signal)

    # FFT
    freqs = np.fft.rfftfreq(len(signal), d=1/fps)

    fft_heart = np.abs(np.fft.rfft(heart_signal))
    fft_resp = np.abs(np.fft.rfft(resp_signal))

    # find peak frequencies
    heart_freq = freqs[np.argmax(fft_heart)]
    resp_freq = freqs[np.argmax(fft_resp)]

    # convert to bpm
    bpm = heart_freq * 60
    respiration_rate = resp_freq * 60

    return bpm, respiration_rate, signal