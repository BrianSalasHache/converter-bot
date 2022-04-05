from googletrans import Translator
from os import system, remove

from config import languages, types
from converter import audios, images
from helpers import file

def translator(language_code: str, delete: bool) -> None:
    for file_found in file.seeker('txt'):
        name, ext = file_found
        print(f'Traduciendo el archivo a {name}.{ext} ...')
        with open(f'{file.folder}{name}.{ext}', 'r', encoding='utf-8') as f:
            text_file = f.read()
        t = Translator().translate(text_file, dest=language_code)
        with open(f'{file.folder}{name}-{language_code}.{ext}', 'w+', encoding='utf-8') as new_file:
            new_file.write(t.text)
        print('Traducción del archivo exitosa!!\n')
        if delete:
            remove(f'{file.folder}{name}.{ext}')
    print('================================\n')

def language(delete: bool = False) -> None:
    option = ' '
    while option not in (languages.translator):
        option = input('SELECCIONE EL LENGUAJE AL QUE QUIERE TRADUCIR:\n\n1. English\n2. Español\t(Spanish)\n3. Français\t(French)\n4. Italiano\t(Italian)\n5. Pусский\t(Russian)\n6. Portugues\t(Portuguese)\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        translator(languages.translator[option], delete)

def options() -> None:
    option = ' '
    while option not in (types.translator):
        option = input('TRADUCIR\n\n 1. Audio\n 2. Imagen\n 3. Texto\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        if option == '3':
            language()
        else:
            func = audios.language if option == '1' else images.language
            if func() == True:
                language(True)