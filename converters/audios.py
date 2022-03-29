from pydub import AudioSegment as AudS
from speech_recognition import AudioFile, Recognizer as r
from traceback import print_exc
from os import system as s, remove

from helpers.seeker_file import seeker, folder

def convert_audio(extension: str) -> None:
    for i in seeker(('mp3', 'wav', 'm4a')):
        name, ext = i
        try:
            print(f'Convirtiendo el archivo a {name}.{ext} a {(extension).upper()}...')
            track = AudS.from_file(f'{folder}{name}.{ext}', format= ext)
            track.export(f'{folder}{name}.{extension}', format= extension)
            print('Conversión del archivo exitosa!!\n')
        except:
            print(f'Falló la conversión del archivo: {name}.{ext}\n')
            print_exc()
            print('')
    print('================================\n')

def convert_audio_string(language_code: str) -> None:
    convert_audio('wav')
    for i in seeker('wav'):
        name, ext = i
        try:
            print(f'Convirtiendo el archivo a {name}.{ext} a TXT...')
            with AudioFile(f'{folder}{name}.{ext}') as source:
                text = r().recognize_google(r().listen(source), language=language_code)
                with open(f'{folder}{name}.txt', 'w', encoding='utf-8') as file:
                    file.write(text)
                print('Conversión del archivo exitosa!!\n')
        except:
            print(f'Falló la conversión del archivo: {name}.{ext}\n')
            print_exc()
            print('')
        finally:
            remove(f'{folder}{name}.{ext}')
    print('================================\n')

def audio_language() -> None:
    option = ' '
    while option not in ('1', '2', '3', '4', '5', '6', '7', '0'):
        option = input('SELECCIONE EL LENGUAJE DEL AUDIO\n\n 1. English\t(United States)\n 2. English\t(United Kingdom)\n 3. Español\t(Argentina)\n 4. Español\t(Spain)\n 5. Français\t(France)\n 6. Italiano\t(Italy)\n 7. Portugues\t(Brazil)\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            convert_audio_string('en-US')
        elif option == '2':
            convert_audio_string('en-GB')
        elif option == '3':
            convert_audio_string('es-AR')
        elif option == '4':
            convert_audio_string('es-ES')
        elif option == '5':
            convert_audio_string('fr-FR')
        elif option == '6':
            convert_audio_string('it-IT')
        elif option == '7':
            convert_audio_string('pt-BR')

def audios_options() -> None:
    option = ' '
    while option not in ('1', '2', '3', '0'):
        option = input('CONVERTIR AUDIO A\n\n 1. MP3  (Audio)\n 2. WAV  (Audio)\n 3. TXT  (Texto)\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            convert_audio('mp3')
        elif option == '2':
            convert_audio('wav')
        elif option == '3':
            audio_language()