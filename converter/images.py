from os import system

from PIL import Image
from pytesseract import pytesseract, image_to_string

from config import extensions, languages, types
from helpers import file


def image(extension: str, message: bool = False) -> None:
    '''Convierte el/los archivo/s de imagen a PNG, JPG o JPEG.'''
    for file_found in file.seeker(extensions.images):
        route, name, ext = file_found
        old_route = f'{route}.{ext}'
        new_route = f'{route}.{extension}'

        if message:
            print(name)

        img = Image.open(old_route).convert('RGB')
        img.save(new_route)


def to_string(
        extension: str,
        language_code: str,
        message: bool = False) -> None:
    '''Convierte el/los archivo/s de imagen a TXT.'''
    for file_found in file.seeker(extensions.images):
        route, name, ext = file_found
        old_route = f'{route}.{ext}'
        new_route = f'{route}.{extension}'

        if message:
            print(name)

        img = Image.open(old_route)
        text = image_to_string(img, lang=language_code, config='--psm 1')
        with open(new_route, 'w+', encoding='utf-8') as new_file:
            new_file.write(text)


pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def language(ext: str, message: bool = False) -> bool:
    '''Elige el idioma de traducción.'''
    option = ' '
    while option not in languages.images:
        option = input(
            'SELECCIONE EL LENGUAJE DE LA IMAGEN:\n\n '
            '1. English\n 2. Español\t(Spanish)\n 3. Français\t(French)\n '
            '4. Italiano\t(Italian)\n 5. Pyccкий\t(Russian)\n '
            '6. Portugues\t(Portuguese)\n\n0. Volver\n\n')
        system('cls')
    activator = False
    if option != '0':
        if message:
            file.decorator(
                to_string,
                extension=ext,
                language_code=languages.images[option],
                message=message)
        else:
            print('Cargando ...')
            to_string(extension=ext, language_code=languages.images[option])
            system('cls')
        activator = True
    return activator


def options() -> None:
    '''Elige la opción de conversión de imagen.'''
    option = ' '
    while option not in types.images:
        option = input(
            'CONVERTIR IMAGEN A\n\n '
            '1. PNG  (Imagen)\n 2. JPG  (Imagen)\n 3. JPEG (Imagen)\n '
            '4. TXT  (Texto)\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        if option == '4':
            language(types.images[option], message=True)
        else:
            file.decorator(image, extension=types.images[option], message=True)
