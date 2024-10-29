import librosa
import numpy as np
import soundfile as sf
from scipy.signal import fftconvolve

print("Loading Pi1 audio file...")
audio_pi1, sr1 = librosa.load("output_2024-10-17_170735.481051.wav", sr=None)
print("Pi1 audio loaded.")

print("Loading Pi2 audio file...")
audio_pi2, sr2 = librosa.load("Valentin1.wav", sr=None)
print("Pi2 audio loaded.")

if sr1 != sr2:
    raise ValueError("Sample rates of the two files do not match")

# Trim silence
print("Trimming silence from both audio files...")
audio_pi1, _ = librosa.effects.trim(audio_pi1)
audio_pi2, _ = librosa.effects.trim(audio_pi2)

# Cross-correlation using FFT
print("Computing cross-correlation with FFT...")
correlation = fftconvolve(audio_pi1, audio_pi2[::-1], mode='full')
lag = np.argmax(correlation) - len(audio_pi2)
print(f"Detected delay: {lag / sr1} seconds")

# Align the audio files
print("Aligning audio files...")
if lag > 0:
    aligned_pi1 = audio_pi1[lag:]
    aligned_pi2 = audio_pi2
else:
    aligned_pi1 = audio_pi1
    aligned_pi2 = audio_pi2[-lag:]

min_length = min(len(aligned_pi1), len(aligned_pi2))
aligned_pi1 = aligned_pi1[:min_length]
aligned_pi2 = aligned_pi2[:min_length]

print("Combining aligned audio into stereo format...")
combined_audio = np.vstack((aligned_pi1, aligned_pi2))

print("Saving aligned audio files...")
sf.write("aligned_pi1.wav", aligned_pi1, sr1)
sf.write("aligned_pi2.wav", aligned_pi2, sr1)

# Save a stereo version
sf.write("aligned_stereo.wav", combined_audio.T, sr1)

print("Processing and saving completed.")