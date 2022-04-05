import msvcrt
import pyaudio
import wave

from speech_recognition import AudioFile, Recognizer
from os import system, remove

from config import languages, types
from converter import translator
from helpers import file

def recorder() -> str:
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True, frames_per_buffer=1024)
    print('Grabando...')
    frames = []
    print('Presione enter para continuar...')
    while not msvcrt.kbhit():
        data = stream.read(1024)
        frames.append(data)
    
    name = file.namer()
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    waveFile = wave.open(f'{file.folder}{name}.wav', 'wb')
    waveFile.setnchannels(2)
    waveFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    waveFile.setframerate(44100)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    print(f'Creación del archivo {name}.wav exitosa!!')
    print('================================\n')
    return name

def to_string(language_code: str) -> None:
    name = recorder()
    with AudioFile(f'{file.folder}{name}.wav') as source:
        text = Recognizer().recognize_google(Recognizer().record(source), language=language_code).lower()
    system('cls')
    with open(f'{file.folder}{name}.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(text)
        print(f'Creación del archivo {name}.txt exitosa!!')
    remove(f'{file.folder}{name}.wav')
    print('================================\n')

def to_string_options(*args) -> None:
    option = ' '
    while option not in (languages.aud_rec):
        option = input('SELECCIONE EL LENGUAJE DE LA GRABACION\n\n 1. English\t(United States)\n 2. English\t(United Kingdom)\n 3. Español\t(Argentina)\n 4. Español\t(España)\n 5. Français\t(France)\n 6. Italiano\t(Italy)\n 7. Portugues\t(Brazil)\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        to_string(languages.aud_rec[option])
        translator.language(True) if args else None

def options() -> None:
    option = ' '
    while option not in (types.recorder):
        option = input('GRABAR\n\n 1. Audio\n 2. Texto\n 3. Texto Traducido\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        if option == '1':
            recorder()
        else:
            to_string_options('trans') if option == '3' else to_string_options()