from moviepy import editor
from traceback import print_exc
from os import system as s

from helpers.seeker_file import seeker, folder

def converter_video(extension: str) -> None:
    for i in seeker(('3g2', '3gp', 'avi', 'flv', 'mkv', 'mov', 'mp4', 'mpg', 'mpeg', 'ogg', 'webm', 'wmv')):
        name, ext = i
        try:
            print(f'Convirtiendo el archivo a {name}.{ext} a {(extension).upper()}...')
            clip = editor.VideoFileClip(f'{folder}{name}.{ext}')
            option = clip.audio.write_audiofile if extension in {'mp3', 'wav'} else clip.write_videofile
            option(f'{folder}{name}.{extension}')
            print('Conversión del archivo exitosa!!\n')
        except:
            print(f'Falló la conversión del archivo: {name}.{ext}\n')
            print_exc()
            print('')
    print('================================\n')

def videos_options() -> None:
    option = ' '
    while option not in ('1', '2', '0'):
        option = input('CONVERTIR:\n\n1. a MP4\n2. a WEBM\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            converter_video('mp4')
        elif option == '2':
            converter_video('webm')

def videos_audios_options() -> None:
    option = ' '
    while option not in ('1', '2', '0'):
        option = input('CONVERTIR:\n\n1. a MP3\n2. a WAV\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            converter_video('mp3')
        elif option == '2':
            converter_video('wav')