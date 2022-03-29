from googletrans import Translator
from traceback import print_exc
from os import system as s, remove

from helpers.seeker_file import seeker, folder
from converters.audios import audio_language
from converters.images import images_string_options

def translator(language_code: str, option: int) -> None:
    for i in seeker('txt'):
        name, ext = i
        try:
            print(f'Traduciendo el archivo a {name}.{ext} ...')
            with open(f'{folder}{name}.{ext}', 'r', encoding='utf-8') as f:
                text_file = f.read()
            t = Translator().translate(text_file, dest=language_code)
            with open(f'{folder}{name}-{language_code}.{ext}', 'w+', encoding='utf-8') as file:
                file.write(t.text)
            print('Traducción del archivo exitosa!!\n')
        except:
            print(f'Falló la traducción del archivo: {name}.{ext}\n')
            print_exc()
            print('')
        finally:
            if option == 1:
                remove(f'{folder}{name}.{ext}')
    print('================================\n')

def translator_language(opt: int) -> None:
    option = ' '
    while option not in ('1', '2', '3', '4', '5', '6', '0'):
        option = input('SELECCIONE EL LENGUAJE AL QUE QUIERE TRADUCIR:\n\n1. English\n2. Español\t(Spanish)\n3. Français\t(French)\n4. Italiano\t(Italian)\n5. Pусский\t(Russian)\n6. Portugues\t(Portuguese)\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            translator('en', opt)
        elif option == '2':
            translator('es', opt)
        elif option == '3':
            translator('fr', opt)
        elif option == '4':
            translator('it', opt)
        elif option == '5':
            translator('ru', opt)
        elif option == '6':
            translator('pt', opt)

def translator_options() -> None:
    option = ' '
    while option not in ('1', '2', '3', '0'):
        option = input('TRADUCIR\n\n 1. Audio\n 2. Imagen\n 3. Texto\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            audio_language()
            translator_language(1)
        elif option == '2':
            images_string_options()
            translator_language(1)
        elif option == '3':
            translator_language(0)