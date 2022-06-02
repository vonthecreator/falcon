#!/usr/bin/python3
from pydub import AudioSegment
from multiprocessing import Pool
from timeit import default_timer as timer

import os


# inputfile.flac, flac, outputfile.mp3, mp3
def transcode_audio(input, ifmt, ofmt):
    audio_input = AudioSegment.from_file(input + ifmt, ifmt.strip('.'))
    return audio_input.export("./output_folder/" + os.path.basename(input), format=ofmt)

def scanner(directory):
    for file in os.scandir(directory):
        if file.is_file():
            file_descr = os.path.splitext(file.path)
            filename = file_descr[0]
            extention = file_descr[1]
            transcode_audio(filename, extention, "mp3")


start = timer()
scanner('./audio_tracks/')
end = timer() - start
print("Transcoding Compelete! \n"+ str(end) + "s")
