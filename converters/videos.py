from moviepy import editor
from os import system as s

from helpers.seeker_file import seeker, folder

# clip = editor.VideoFileClip('../conversor/prueba.mp4')

# clip.write_videofile('../conversor/prueba.webm')

def converter_video(extension_1: str, extension_2: str) -> None:
    for i in seeker(extension_1, extension_2):
        name, ext, ext2 = i
        clip = editor.VideoFileClip(f"{folder}{name}.{ext}")
        clip.write_videofile(f'{folder}{name}.{ext2}')

def videos_options():
    option = ' '
    while option not in ('1', '2', '3', '4', '0'):
        option = input('CONVERTIR:\n\n1. De avi a mp4\n2. De mkv a mp4\n3. De mpeg a mp4\n4. De webm a mp4\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            converter_video('avi', 'mp4')
        elif option == '2':
            converter_video('mkv', 'mp4')
        elif option == '3':
            converter_video('mpeg', 'mp4')
        elif option == '4':
            converter_video('webm', 'mp4')