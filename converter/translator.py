from os import system, remove

from googletrans import Translator

from config import languages, types
from converter import audios, images
from helpers import file


def translator(
        language_code: str,
        delete: bool,
        message: bool = False) -> None:
    '''Traduce el/los archivo/s de audio, imagen o texto a otro idioma.'''
    for file_found in file.seeker('txt'):
        route, name, ext = file_found
        old_route = f'{route}.{ext}'
        new_route = f'{route}-{language_code}.{ext}'

        if message:
            print(name)

        with open(old_route, 'r', encoding='utf-8') as f:
            text_file = f.read()
        t = Translator().translate(text_file, dest=language_code)

        with open(new_route, 'w+', encoding='utf-8') as new_file:
            new_file.write(t.text.lower())

        if delete:
            remove(old_route)


def language(delete: bool = False, message: bool = False) -> None:
    '''Selecciona el idioma de traducción.'''
    option = ' '
    while option not in languages.translator:
        option = input(
            'SELECCIONE EL LENGUAJE AL QUE QUIERE TRADUCIR:\n\n '
            '1. English\n 2. Español\t(Spanish)\n 3. Français\t(French)\n '
            '4. Italiano\t(Italian)\n 5. Pyccкий\t(Russian)\n '
            '6. Portugues\t(Portuguese)\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        if message:
            file.decorator(
                translator,
                language_code=languages.translator[option],
                delete=delete,
                message=True,
                msg='Traduciendo')
        else:
            print('Cargando ...')
            translator(
                language_code=languages.translator[option],
                delete=delete)
            system('cls')


def options() -> None:
    '''Elige la opción a traducir.

    Si la opción es 1, convierte el/los audio/s a TXT y luego lo/s traduce.
    Si la opción es 2, convierte la/s imagen/es a TXT y luego la/s traduce.
    '''
    option = ' '
    while option not in types.translator:
        option = input(
            'TRADUCIR\n\n '
            '1. Audio\n 2. Imagen\n 3. Texto\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        if option == '3':
            language()
        else:
            func = audios.language if option == '1' else images.language
            if func(types.translator[option]):
                language(True)
