from speech_recognition import Recognizer as r, Microphone, UnknownValueError
import re
from datetime import datetime
from traceback import print_exc
from os import system as s

from helpers.seeker_file import folder
from converters.translator import translator_language

def convert_recording_string(language_code: str):
    while True:
        try:
            print('Grabando...')
            with Microphone() as mic:
                r().adjust_for_ambient_noise(mic, duration=0.2)
                text = r().recognize_google(r().listen(mic), language=language_code).lower()
            s('cls')
            while True:
                s('cls')
                name = input('Caracteres especiales permitidos: "_", "-" y (espacio)\nElija el nombre del archivo:')
                if re.match('^[a-zA-Z 0-9ñ_-]*$', name):
                    break
            if name == '':
                name = 'Grabacion ' + datetime.now().strftime("%d-%m-%Y %H-%M")
            with open(f'{folder}{name}.txt', 'w', encoding='utf-8') as file:
                file.write(text)
                print(f'Creación del archivo {name}.txt exitosa!!')
        except UnknownValueError:
            s('cls')
            print("Tenes que hablar:")
            continue
        except:
            print("Falló la creación del archivo")
            print_exc()
        break
    print('================================\n')

def recorder_language() -> None:
    option = ' '
    while option not in ('1', '2', '3', '4', '5', '6', '7', '0'):
        option = input('SELECCIONE EL LENGUAJE DE LA GRABACION\n\n 1. English\t(United States)\n 2. English\t(United Kingdom)\n 3. Español\t(Argentina)\n 4. Español\t(Spain)\n 5. Français\t(France)\n 6. Italiano\t(Italy)\n 7. Portugues\t(Brazil)\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            convert_recording_string('en-US')
        elif option == '2':
            convert_recording_string('en-GB')
        elif option == '3':
            convert_recording_string('es-AR')
        elif option == '4':
            convert_recording_string('es-ES')
        elif option == '5':
            convert_recording_string('fr-FR')
        elif option == '6':
            convert_recording_string('it-IT')
        elif option == '7':
            convert_recording_string('pt-BR')

def recorder_options() -> None:
    option = ' '
    while option not in ('1', '2', '0'):
        
        option = input('CONVERTIR GRABACION A TEXTO\n\n 1. Original\n 2. Traducido\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            recorder_language()
        elif option == '2':
            recorder_language()
            translator_language(1)