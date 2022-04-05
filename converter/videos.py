from moviepy import editor
from os import system

from config import extensions, types
from helpers import file

def video(extension: str) -> None:
    for file_found in file.seeker(extensions.videos):
        name, ext = file_found
        print(f'Convirtiendo el archivo a {name}.{ext} a {(extension).upper()}...')
        clip = editor.VideoFileClip(f'{file.folder}{name}.{ext}')
        option = clip.audio.write_audiofile if extension in {'mp3', 'wav'} else clip.write_videofile
        option(f'{file.folder}{name}.{extension}')
        print('Conversión del archivo exitosa!!\n')
    print('================================\n')

def options() -> None:
    option = ' '
    while option not in (types.videos):
        option = input('CONVERTIR VIDEO A\n\n 1. MP3  (Audio)\n 2. WAV  (Audio)\n 3. MP4  (Video)\n 4. WEBM (Video)\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        video(types.videos[option])