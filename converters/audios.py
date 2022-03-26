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

def convert_audio_text(extension: str, language_code: str) -> None:
    convert_audio('wav')
    for i in seeker('wav'):
        name, ext = i
        try:
            print(f'Convirtiendo el archivo a {name}.{ext} a {(extension).upper()}...')
            with AudioFile(f'{folder}{name}.{ext}') as source:
                text = r().recognize_google(r().listen(source), language=language_code)
                with open(f'{folder}{name}.{extension}', 'w') as file:
                    file.write(text)
                print('Conversión del archivo exitosa!!\n')
        except:
            print(f'Falló la conversión del archivo: {name}.{ext}\n')
            print_exc()
            print('')
        finally:
            remove(f'{folder}{name}.{ext}')
    print('================================\n')

def audios_options() -> None:
    option = ' '
    while option not in ('1', '2', '0'):
        option = input('CONVERTIR:\n\n1. a MP3\n2. a WAV\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            convert_audio('mp3')
        elif option == '2':
            convert_audio('wav')

def audio_text_options() -> None:
    option = ' '
    while option not in ('1', '2', '3', '4', '5', '6', '7', '0'):
        option = input('SELECCIONE EL LENGUAJE DEL AUDIO POR FAVOR:\n\n1. English\t(United States)\n2. English\t(United Kingdom)\n3. Español\t(Argentina)\n4. Español\t(Spain)\n5. Français\t(France)\n6. Italiano\t(Italy)\n7. Portugues\t(Brazil)\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            convert_audio_text('txt', 'en-US')
        elif option == '2':
            convert_audio_text('txt', 'en-GB')
        elif option == '3':
            convert_audio_text('txt', 'es-AR')
        elif option == '4':
            convert_audio_text('txt', 'es-ES')
        elif option == '5':
            convert_audio_text('txt', 'fr-FR')
        elif option == '6':
            convert_audio_text('txt', 'it-IT')
        elif option == '7':
            convert_audio_text('txt', 'pt-BR')