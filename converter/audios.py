from os import system, remove
from typing import Tuple

from pydub import AudioSegment
from speech_recognition import AudioFile, Recognizer

from config import extensions, languages, types
from helpers import file


def audio(extension: str, message: bool = False) -> Tuple[str, str, str]:
    '''Convierte el/los archivo/s de audio a MP3 o WAV.'''
    for file_found in file.seeker(extensions.audios):
        route, name, ext = file_found
        old_route = f'{route}.{ext}'
        new_route = f'{route}.{extension}'

        if message:
            print(name)

        track = AudioSegment.from_file(old_route, ext)
        track.export(new_route, extension)
    return route, name, extension


def to_string(
        extension: str,
        language_code: str,
        message: bool = False) -> None:
    '''Convierte el/los archivo/s de audio a TXT.'''
    for file_found in file.seeker(extensions.audios):
        route, name, ext = file_found
        delete = False
        if ext != 'wav':
            route, name, ext = audio('wav')
            delete = True
        old_route = f'{route}.{ext}'
        new_route = f'{route}.{extension}'

        if message:
            print(name)

        with AudioFile(old_route) as source:
            r = Recognizer()
            aud = r.record(source)
            text = r.recognize_google(aud, language=language_code).lower()

            with open(new_route, 'w', encoding='utf-8') as new_file:
                new_file.write(text)
        if delete:
            remove(old_route)


def language(ext: str, message: bool = False) -> bool:
    '''Elige el idioma del audio.'''
    option = ' '
    while option not in languages.aud_rec:
        option = input(
            'SELECCIONE EL LENGUAJE DEL AUDIO\n\n '
            '1. English\t(United States)\n 2. English\t(United Kingdom)\n '
            '3. Español\t(Argentina)\n 4. Español\t(Spain)\n '
            '5. Français\t(France)\n 6. Italiano\t(Italy)\n '
            '7. Portugues\t(Brazil)\n\n0. Volver\n\n')
        system('cls')
    activador = False
    if option != '0':
        if message:
            file.decorator(
                to_string,
                extension=ext,
                language_code=languages.aud_rec[option],
                message=message)
        else:
            print('Cargando ...')
            to_string(extension=ext, language_code=languages.aud_rec[option])
            system('cls')
        activador = True
    return activador


def options() -> None:
    '''Elige la opción de conversión de audio.'''
    option = ' '
    while option not in types.audios:
        option = input(
            'CONVERTIR AUDIO A\n\n '
            '1. MP3  (Audio)\n 2. WAV  (Audio)\n 3. TXT  (Texto)\n\n'
            '0. Volver\n\n')
        system('cls')
    if option != '0':
        if option == '3':
            language(types.audios[option], message=True)
        else:
            file.decorator(audio, extension=types.audios[option], message=True)
