import csv
import numpy as np

def read_frequencies_and_amplitudes(file_path):
    frequencies = []
    amplitudes = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip header row

        for row in reader:
            frequency = float(row[0].replace(',', '.'))
            amplitude = float(row[1].replace(',', '.'))
            frequencies.append(frequency)
            amplitudes.append(amplitude)


    return frequencies, amplitudes


def getSpectre():
    frequencies = []
    amplitudes = []
    phases = []

    frequencie, amplitude = read_frequencies_and_amplitudes('spectrogram_notes/note0_16kechantillon.txt')
    random_phase_list = np.random.uniform(0, 2 * np.pi, len(frequencie)).tolist()
    phases.append(random_phase_list)
    frequencies.append(frequencie)
    amplitudes.append(amplitude)

    frequencie, amplitude = read_frequencies_and_amplitudes('spectrogram_notes/note1_16kechantillon.txt')
    random_phase_list = np.random.uniform(0, 2 * np.pi, len(frequencie)).tolist()
    phases.append(random_phase_list)
    frequencies.append(frequencie)
    amplitudes.append(amplitude)

    frequencie, amplitude = read_frequencies_and_amplitudes('spectrogram_notes/note2_8kechantillon.txt')
    random_phase_list = np.random.uniform(0, 2 * np.pi, len(frequencie)).tolist()
    phases.append(random_phase_list)
    frequencies.append(frequencie)
    amplitudes.append(amplitude)

    frequencie, amplitude = read_frequencies_and_amplitudes('spectrogram_notes/note3_8kechantillon.txt')
    random_phase_list = np.random.uniform(0, 2 * np.pi, len(frequencie)).tolist()
    phases.append(random_phase_list)
    frequencies.append(frequencie)
    amplitudes.append(amplitude)

    frequencie, amplitude = read_frequencies_and_amplitudes('spectrogram_notes/note4_16kechantillon.txt')
    random_phase_list = np.random.uniform(0, 2 * np.pi, len(frequencie)).tolist()
    phases.append(random_phase_list)
    frequencies.append(frequencie)
    amplitudes.append(amplitude)

    frequencie, amplitude = read_frequencies_and_amplitudes('spectrogram_notes/note5_8kechantillon.txt')
    random_phase_list = np.random.uniform(0, 2 * np.pi, len(frequencie)).tolist()
    phases.append(random_phase_list)
    frequencies.append(frequencie)
    amplitudes.append(amplitude)

    amplitudes = db_to_linear(amplitudes)

    data_commbined = {
        'frequency': frequencies,
        'amplitude': amplitudes,
        'phase': phases
    }
    
    return data_commbined
    
def db_to_linear(amplitudes_db):
    if isinstance(amplitudes_db, (list, np.ndarray)):
        if all(isinstance(i, (list, np.ndarray)) for i in amplitudes_db):
            # Traitement d'un tableau 2D non homogène
            return [db_to_linear(sublist) for sublist in amplitudes_db]
        else:
            # Traitement d'un tableau 1D
            return 10 ** (np.array(amplitudes_db) / 20)
    else:
        raise ValueError("Input must be a list or numpy array")



if __name__ == "__main__":
    # Exemple d'utilisation
    file_path = 'note0.txt'  # Remplacez par le chemin vers votre fichier CSV

    frequencies, amplitudes_linear = read_frequencies_and_amplitudes(file_path)

    print("Fréquences :", frequencies)
    print("Amplitudes linéaires :", amplitudes_linear)