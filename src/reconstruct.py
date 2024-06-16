import numpy as np
from pydub import AudioSegment
from scipy.fft import fft, ifft
from scipy.signal import istft
from pydub.generators import Sine
import librosa
import librosa.display
import math

def reconstruct_signal_note(frequencie,amplitude, phase, length_signal=1000, sample_rate=44100):
    duration = length_signal / sample_rate
    time = np.linspace(0, duration, length_signal, endpoint=False)
    
    reconstructed_signal = np.zeros(length_signal)

    window_time = time[0: length_signal]
    window_signal = np.zeros(length_signal)
    
    for freq, ampl, phase in zip(frequencie, amplitude, phase):
        window_signal += ampl * np.sin(2 * np.pi * freq * window_time + phase)
    
    reconstructed_signal[0: 1 * length_signal] = window_signal
  
    reconstructed_signal /= np.max(np.abs(reconstructed_signal))
    return reconstructed_signal
    

def reconstruct_audio_segment(notes, data, length_signal = 1000, sample_rate=44100):
    all_signals = []
    for i in range(len(data['note'])):
        if(data['durations'][i]!=0):
            if(data['note'][i]!=0):
                note = int(math.log2(data['note'][i]))
                note = 5 - note
                print(note," ",data['durations'][i])
                frequency = notes['frequency'][note]
                amplitude = notes['amplitude'][note]  # Par exemple, vous pouvez fixer une amplitude ici
                phase = notes['phase'][note]      # Par exemple, vous pouvez fixer une phase ici
                length_signal = int((data['durations'][i] * sample_rate)/1000)  # Calcul de la longueur du signal en fonction de la durée
                # Appel de la fonction reconstruct_signal_note avec les paramètres appropriés
                signal_rec = reconstruct_signal_note(frequency, amplitude, phase, length_signal, sample_rate)
                all_signals = np.append(all_signals, signal_rec)
            else:
                length_signal = int((data['durations'][i] * sample_rate)/1000)
                new_signals = np.zeros(length_signal)
                all_signals = np.append(all_signals, new_signals)

    # Convertir en un format que pydub peut utilise
    audio_segment = AudioSegment(
        (all_signals * 32767).astype(np.int16).tobytes(),
        frame_rate=sample_rate,
        sample_width=2,
        channels=1
    )
    return audio_segment

def save_audio_to_mp3(audio_segment, file_path):
    audio_segment.export(file_path, format="mp3")



if __name__ == "__main__":

    print("Audio file has been reconstructed and saved as 'reconstructed_audio.mp3'.")