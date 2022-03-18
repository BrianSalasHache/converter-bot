from pydub import AudioSegment
from os import system

from helpers.seeker_file import seeker

def converter_audio(ext1, ext2):
    for i in seeker(ext1, ext2):
        if i[1] == 'wav':
            audio = AudioSegment.from_wav(f"./conversor/{i[0]}.{i[1]}")
        elif i[1] == 'mp3':
            audio = AudioSegment.from_mp3(f"./conversor/{i[0]}.{i[1]}")
        audio.export(f"./conversor/{i[0]}.{i[2]}", format=f"{i[2]}")

def audios_options():
    option = ' '
    while option not in ('1', '2', '0'):
        option = input('CONVERTIR:\n\n1. De mp3 a wav\n2. De wav a mp3\n\n0. Volver\n\n')
        system('cls')

        if option == '1':
            converter_audio('mp3', 'wav')
        elif option == '2':
            converter_audio('wav', 'mp3')