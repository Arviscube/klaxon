import numpy as np
from pydub import AudioSegment
from scipy.fft import fft
import reconstruct
import matplotlib.pyplot as plt


def get_dominant_frequencies(audio_file, window_size=1000, sample_rate=44100):
    # Charger le fichier audio
    audio = AudioSegment.from_file(audio_file, format="mp3")
    
    # Convertir en échantillons numpy
    samples = np.array(audio.get_array_of_samples())
    
    # Utiliser uniquement un canal s'il y en a plusieurs
    if audio.channels > 1:
        samples = samples[::audio.channels]
    
    # Nombre d'échantillons
    n_samples = len(samples)

    # Nombre de fenêtres
    n_windows = n_samples // window_size
    
    # Liste pour stocker les fréquences dominantes
    all_dominant_frequencies = []
    all_dominant_amplitudes = []
    all_dominant_phases = []

    bitDeth = (audio.sample_width * 8)
    positiveBitDeph = bitDeth - 1
    max_sample_value = 2 ** positiveBitDeph
    
    for i in range(n_windows):
        # Extraire la fenêtre
        window_samples = samples[i * window_size : (i + 1) * window_size]
        
        # Appliquer la FFT
        fft_result = fft(window_samples)
        
        # Obtenir les fréquences correspondantes
        freqs = np.fft.fftfreq(len(window_samples), 1 / sample_rate)
        
        # Obtenir les amplitudes correspondantes
        magnitudes = np.abs(fft_result)
        
        # Obtenir les phases correspondantes
        phases = np.angle(fft_result)
        
        # Filtrer les fréquences positives
        positive_freqs = freqs[:len(freqs) // 2]
        positive_magnitudes = magnitudes[:len(magnitudes) // 2]
        positive_phases = phases[:len(phases) // 2]

        # Supprimer les fréquences au-dessus de 15000 Hz
        # freq_mask = positive_freqs <= 15000
        # positive_freqs = positive_freqs[freq_mask]
        # positive_magnitudes = positive_magnitudes[freq_mask]
        # positive_phases = positive_phases[freq_mask]
        
        # Trouver les indices des 10 fréquences dominantes
        dominant_indices = np.argsort(positive_magnitudes)[-20:][::-1]
        
        # Ajouter les fréquences dominantes à la liste
        dominant_frequencies = positive_freqs[dominant_indices]
        dominant_amplitudes = positive_magnitudes[dominant_indices]
        dominant_phases = positive_phases[dominant_indices]

        dominant_amplitudes_normalized = dominant_amplitudes / max_sample_value

        all_dominant_frequencies.append(dominant_frequencies)
        all_dominant_amplitudes.append(dominant_amplitudes_normalized)
        all_dominant_phases.append(dominant_phases)
    
    return all_dominant_frequencies, all_dominant_amplitudes, all_dominant_phases



def plot_frequency_distribution(frequencies):
    # Convertir le tableau 2D en une seule liste
    all_frequencies = [freq for window in frequencies for freq in window]

    # Créer l'histogramme
    plt.hist(all_frequencies, bins=20, color='blue', edgecolor='black')

    # Ajouter des titres et des étiquettes
    plt.title('Répartition des fréquences audio')
    plt.xlabel('Fréquence (Hz)')
    plt.ylabel('Nombre d\'occurrences')
    plt.grid(True)

    # Afficher l'histogramme
    plt.show()




if __name__ == "__main__":

    # Exemple d'utilisation
    audio_file = 'VID_133770519_123928_341.mp3'
    # audio_file = 'musique du film ( La 7eme Compagnie).mp3'
    window_size = 1000
    dominant_frequencies,dominant_amplitudes, dominant_phases = get_dominant_frequencies(audio_file,window_size)


    print("Dominant frequencies per window:")
    for window_idx, (frequencies, amplitudes, phases) in enumerate(zip(dominant_frequencies, dominant_amplitudes, dominant_phases)):
        print(f"Window {window_idx+1}:")
        print(f"{frequencies}")
        print(f"{amplitudes}")
        print(f"{phases}")
        print(f"----------------------------------------------")

    plot_frequency_distribution(dominant_frequencies)    

    # dominant_frequencies_int = dominant_frequencies.astype(int)


    audio_segment = reconstruct.reconstruct_audio_segment(dominant_frequencies,dominant_amplitudes,dominant_phases,window_size)
    reconstruct.save_audio_to_mp3(audio_segment, 'reconstructed_audio.mp3')

    ##lastFrequency
    all_dominant_frequencies = []
    all_dominant_amplitudes = []
    all_dominant_phases = []
    all_dominant_frequencies.append(dominant_frequencies[-1])
    print(dominant_frequencies[-1])
    all_dominant_amplitudes.append(dominant_amplitudes[-1])
    print(dominant_amplitudes[-1])
    all_dominant_phases.append(np.zeros(10))
    audio_segment = reconstruct.reconstruct_audio_from_frequencies(all_dominant_frequencies,all_dominant_amplitudes,44100)
    reconstruct.save_audio_to_mp3(audio_segment, 'reconstructed_audio1SS.mp3')
    #####################################