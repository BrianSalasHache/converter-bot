from pydub import AudioSegment as AudS
from os import system as s

from helpers.seeker_file import seeker, folder

def converter_audio(extension_1: str, extension_2: str) -> None:
    for i in seeker(extension_1, extension_2):
        name, ext, ext2 = i
        convert = AudS.from_wav if ext == 'wav' else AudS.from_mp3 if ext == 'mp3' else None
        audio = convert(f'{folder}{name}.{ext}')
        audio.export(f'{folder}{name}.{ext2}', format=f'{ext2}')

def audios_options() -> None:
    option = ' '
    while option not in ('1', '2', '0'):
        option = input('CONVERTIR:\n\n1. De mp3 a wav\n2. De wav a mp3\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            converter_audio('mp3', 'wav')
        elif option == '2':
            converter_audio('wav', 'mp3')