from os import system, remove

from gtts import gTTS

from config import languages, types
from converter import images
from helpers import file


def reader(
        language: str,
        domain: str,
        delete: bool,
        message: bool = False) -> None:
    '''Lee un archivo de imagen o texto y lo guarda en MP3'''
    for file_found in file.seeker('txt'):
        route, name, ext = file_found
        old_route = f'{route}.{ext}'
        new_route = f'{route}-reader-{language}-{domain}.mp3'

        if message:
            print(name)

        text = open(old_route, 'r', encoding='utf-8').read()
        speech = gTTS(text=text, lang=language, tld=domain, slow=False)
        speech.save(new_route)

        if delete:
            remove(f'{route}.{ext}')


def language(delete: bool = False) -> None:
    '''Elige el idioma del lector.'''
    option = ' '
    while option not in languages.reader:
        option = input(
            'SELECCIONE EL LENGUAJE DEL LECTOR:\n\n '
            '1. English\t(United Kingdom)\n 2. English\t(United States)\n '
            '3. Español\t(Mexico)\n 4. Español\t(España)\n '
            '5. Français\t(France)\n 6. Portugues\t(Brazil)\n '
            '7. Portugues\t(Portugal)\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        language, domain = languages.reader[option]
        file.decorator(
            reader,
            language=language,
            domain=domain,
            delete=delete,
            message=True,
            msg='Leyendo')


def options() -> None:
    '''Elige la opción a leer.

    Si el archivo es una imagen, lo convierte a TXT y luego a MP3.
    '''
    option = ' '
    while option not in types.reader:
        option = input('LEER\n\n '
                       '1. Imagen\n 2. Texto\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        if option == '1' and images.language(types.reader[option]):
            language(True)
        elif option == '2':
            language()
