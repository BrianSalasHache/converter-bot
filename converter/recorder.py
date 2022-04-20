from os import system, remove
from typing import Tuple
import msvcrt

from speech_recognition import AudioFile, Recognizer
import pyaudio
import wave

from config import languages, types
from converter import translator
from helpers import file


def recorder(message: bool = False) -> Tuple[str, str]:
    '''Graba un archivo y lo guarda en WAV.'''
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=2,
        rate=44100,
        input=True,
        frames_per_buffer=1024)
    frames = []

    print('Grabando ...\nPresiona ENTER para continuar ...')
    while not msvcrt.kbhit():
        data = stream.read(1024)
        frames.append(data)

    route, name = file.namer()
    new_route = f'{route}.wav'
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(new_route, 'wb')
    waveFile.setnchannels(2)
    waveFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    waveFile.setframerate(44100)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    system('cls')

    if message:
        print(name)

    return route, name


def to_string(language_code: str, message: bool = False) -> None:
    '''Convierte el archivo WAV a TXT.'''
    route, name = recorder()
    old_route = f'{route}.wav'
    new_route = f'{route}.txt'

    system('cls')
    print('Cargando ...')

    with AudioFile(old_route) as source:
        r = Recognizer()
        aud = r.record(source)
        text = r.recognize_google(aud, language=language_code).lower()
    system('cls')

    if message:
        print(name)

    with open(new_route, 'w', encoding='utf-8') as new_file:
        new_file.write(text)
    remove(old_route)


def to_string_options(*args, message: bool = False) -> None:
    '''Elige el lenguage de grabación para convertirlo a TXT.

    Si se pasa el argumento message, se imprime la creación del archivo.
    Si se pasa el argumento *args, traduce el archivo TXT.
    '''
    option = ' '
    while option not in (languages.aud_rec):
        option = input('SELECCIONE EL LENGUAJE DE LA GRABACION\n\n '
                       '1. English\t(United States)\n '
                       '2. English\t(United Kingdom)\n '
                       '3. Español\t(Argentina)\n 4. Español\t(España)\n '
                       '5. Français\t(France)\n 6. Italiano\t(Italy)\n '
                       '7. Portugues\t(Brazil)\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        if message:
            file.decorator(
                to_string,
                language_code=languages.aud_rec[option],
                message=message,
                msg='')
        else:
            to_string(language_code=languages.aud_rec[option])
            system('cls')
        if args:
            translator.language(delete=True, message=True)


def options() -> None:
    '''Elige la opción a grabar.

    La opción 3 convierte el archivo a TXT y luego lo traduce.
    '''
    option = ' '
    while option not in (types.recorder):
        option = input('GRABAR\n\n '
                       '1. Audio\n 2. Texto\n 3. Texto Traducido\n\n'
                       '0. Volver\n\n')
        system('cls')
    if option != '0':
        if option == '1':
            file.decorator(recorder, message=True, msg='')
        else:
            to_string_options(
                'trans') if option == '3' else to_string_options(message=True)
