import re

def extract_data_from_file(filename):
    note = []
    durations = []

    with open(filename, 'r') as file:
        for line in file:
            # Trouver toutes les occurrences de tuples {0,8} dans la ligne
            matches = re.findall(r'\{(\d+),(\d+)\}', line)

            # Si des correspondances sont trouvées
            if matches:
                for match in matches:
                    freq = int(match[1])
                    duration = int(match[0])
                    note.append(freq)
                    durations.append(duration)

    data_commbined = {
        'note': note,
        'durations': durations,
    }
    
    return data_commbined




if __name__ == "__main__":

    # Exemple d'utilisation
    filename = 'noteFileOriginal/7eCompagnies3.txt'  # Remplacez par le chemin de votre fichier
    data = extract_data_from_file(filename)

    # Afficher les résultats
    print("note:", data['note'])
    print("Durations:", data['durations'])