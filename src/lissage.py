import numpy as np
from pydub import AudioSegment

def smooth_audio(audio_segment, window_size=1000):
    # Convertir l'AudioSegment en un tableau numpy de points de données
    audio_data = np.array(audio_segment.get_array_of_samples())
    
    # Nombre de points de données dans le signal audio
    signal_length = len(audio_data)
    
    # Calculer le nombre de fenêtres
    num_windows = signal_length // window_size
    
    # Initialiser un tableau pour le signal lissé
    smoothed_signal = np.zeros(signal_length)
    
    # Appliquer un lissage par moyenne glissante
    for i in range(num_windows):
        start_idx = i * window_size
        end_idx = start_idx + window_size
        
        # Sélectionner la partie du signal à lisser
        window_data = audio_data[start_idx:end_idx]
        
        # Calculer la moyenne de la fenêtre
        window_average = np.mean(window_data)
        
        # Remplacer la partie du signal lissé par la moyenne de la fenêtre
        smoothed_signal[start_idx:end_idx] = window_average
    
    # Convertir le signal lissé en un format que pydub peut utiliser
    smoothed_audio_segment = AudioSegment(
        (smoothed_signal).astype(np.int16).tobytes(),
        frame_rate=audio_segment.frame_rate,
        sample_width=audio_segment.sample_width,
        channels=audio_segment.channels
    )
    
    return smoothed_audio_segment

# Exemple d'utilisation :
input_file = "testNotes.mp3"
output_file = "testNotesSmouth.mp3"

audio_segment = AudioSegment.from_file(input_file)

# Lissage du signal audio avec une fenêtre de 1000 échantillons
smoothed_audio = smooth_audio(audio_segment, window_size=1000)

# Enregistrer le signal audio lissé
smoothed_audio.export(output_file, format="wav")

print("Lissage terminé. Fichier enregistré:", output_file)