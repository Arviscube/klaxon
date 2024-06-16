import numpy as np
import pyaudio

# Paramètres audio
fs = 44100  # Fréquence d'échantillonnage
duration = 5  # Durée en secondes

# Fréquences des sons
frequencies = [969, 1460, 1950, 2444]

# Génération des ondes sinusoïdales
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
wave = sum(np.sin(2 * np.pi * f * t) for f in frequencies)

# Normalisation
wave = (wave / np.max(np.abs(wave)) * 32767).astype(np.int16)

# Initialisation de PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=fs, output=True)

# Lecture de l'onde sonore
stream.write(wave.tobytes())

# Fermeture du stream et de PyAudio
stream.stop_stream()
stream.close()
p.terminate()