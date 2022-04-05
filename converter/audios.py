from pydub import AudioSegment
from speech_recognition import AudioFile, Recognizer
from os import system, remove

from config import extensions, languages, types
from helpers import file

def audio(extension: str) -> None:
    for file_found in file.seeker(extensions.audios):
        name, ext = file_found
        print(f'Convirtiendo el archivo a {name}.{ext} a {(extension).upper()}...')
        track = AudioSegment.from_file(f'{file.folder}{name}.{ext}', format= ext)
        track.export(f'{file.folder}{name}.{extension}', format= extension)
        print('Conversión del archivo exitosa!!\n')
    print('================================\n')

def to_string(language_code: str) -> None:
    audio('wav')
    for file_found in file.seeker('wav'):
        name, ext = file_found
        print(f'Convirtiendo el archivo a {name}.{ext} a TXT...')
        with AudioFile(f'{file.folder}{name}.{ext}') as source:
            text = Recognizer().recognize_google(Recognizer().record(source), language=language_code)
            with open(f'{file.folder}{name}.txt', 'w', encoding='utf-8') as new_file:
                new_file.write(text)
            print('Conversión del archivo exitosa!!\n')
        remove(f'{file.folder}{name}.{ext}')
    print('================================\n')

def language() -> None:
    option = ' '
    while option not in (languages.aud_rec):
        option = input('SELECCIONE EL LENGUAJE DEL AUDIO\n\n 1. English\t(United States)\n 2. English\t(United Kingdom)\n 3. Español\t(Argentina)\n 4. Español\t(Spain)\n 5. Français\t(France)\n 6. Italiano\t(Italy)\n 7. Portugues\t(Brazil)\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        to_string(languages.aud_rec[option])
        return True

def options() -> None:
    option = ' '
    while option not in (types.audios):
        option = input('CONVERTIR AUDIO A\n\n 1. MP3  (Audio)\n 2. WAV  (Audio)\n 3. TXT  (Texto)\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        language() if option == '3' else audio(types.audios[option])