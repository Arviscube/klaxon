import reconstruct
import readSpectre
import notefile
import numpy as np
from pydub import AudioSegment


notes = readSpectre.getSpectre()

filenameInput = 'noteFileOriginal/7eCompagnies3.txt'
filenameOutput = 'testNotes.mp3'

print("export note frome file " + filenameInput)
data = notefile.extract_data_from_file(filenameInput)
print(f"{len(data['durations'])} notes find")

print("allign segment")
first_frequency = data['durations'].pop(0)
data['durations'].append(first_frequency)

print("create audio segment")
audio_segment = reconstruct.reconstruct_audio_segment(notes,data,44100)
print("save output in " + filenameOutput)
reconstruct.save_audio_to_mp3(audio_segment, filenameOutput)