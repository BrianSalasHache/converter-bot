from os import system

from moviepy.video.fx.crop import crop
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.speedx import speedx
from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy import editor

from config import extensions, types
from helpers import file


def video(extension: str, message: bool = False) -> None:
    '''Convierte el/los archivo/s de video a MP3, WAV, MP4 o WEBM.'''
    for file_found in file.seeker(extensions.videos):
        route, name, ext = file_found
        old_route = f'{route}.{ext}'
        new_route = f'{route}.{extension}'

        if message:
            print(name)

        clip = editor.VideoFileClip(old_route)
        option = clip.audio.write_audiofile if extension in extensions.audios \
            else clip.write_videofile
        option(new_route)


def options() -> None:
    '''Elige la opción de conversión de video.'''
    option = ' '
    while option not in types.videos:
        option = input(
            'CONVERTIR VIDEO A\n\n '
            '1. MP3  (Audio)\n 2. WAV  (Audio)\n 3. MP4  (Video)\n '
            '4. WEBM (Video)\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        file.decorator(video, extension=types.videos[option], message=True)
