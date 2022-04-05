from PIL import Image
from pytesseract import pytesseract, image_to_string
from os import system

from config import extensions, languages, types
from helpers import file

def image(extension: str) -> None:
    for file_found in file.seeker(extensions.images):
        name, ext = file_found
        print(f'Convirtiendo el archivo a {name}.{ext} a {(extension).upper()}...')
        img = Image.open(f'{file.folder}{name}.{ext}').convert('RGB')
        img.save(f'{file.folder}{name}.{extension}')
        print('Conversión del archivo exitosa!!\n')
    print('================================\n')

def to_string(language_code: str, extension: str = 'txt') -> None:
    for file_found in file.seeker(extensions.images):
        name, ext = file_found
        print(f'Convirtiendo el archivo a {name}.{ext} a {(extension).upper()}...')
        text = image_to_string(Image.open(f'{file.folder}{name}.{ext}'), lang=language_code, config='--psm 1')
        with open(f'{file.folder}{name}.{extension}', 'w+', encoding='utf-8') as new_file:
            new_file.write(text)
        print('Conversión del archivo exitosa!!\n')
    print('================================\n')

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def language() -> bool:
    option = ' '
    while option not in (languages.images):
        option = input('SELECCIONE EL LENGUAJE DE LA IMAGEN:\n\n1. English\n2. Español\t(Spanish)\n3. Français\t(French)\n4. Italiano\t(Italian)\n5. Pусский\t(Russian)\n6. Portugues\t(Portuguese)\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        to_string(languages.images[option])
        return True

def options() -> None:
    option = ' '
    while option not in (types.images):
        option = input('CONVERTIR IMAGEN A\n\n 1. PNG  (Imagen)\n 2. JPG  (Imagen)\n 3. JPEG (Imagen)\n 4. TXT  (Texto)\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        language() if option == '4' else image(types.images[option])