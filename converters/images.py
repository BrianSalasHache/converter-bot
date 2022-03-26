from PIL import Image
from pytesseract import pytesseract, image_to_string
from traceback import print_exc
from os import system as s

from helpers.seeker_file import seeker, folder

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def converter_image(extension: str) -> None:
    for i in seeker(('png', 'jpg', 'jpeg')):
        name, ext = i
        try:
            print(f'Convirtiendo el archivo a {name}.{ext} a {(extension).upper()}...')
            img = Image.open(f'{folder}{name}.{ext}').convert('RGB')
            img.save(f'{folder}{name}.{extension}')
            print('Conversión del archivo exitosa!!\n')
        except:
            print(f'Falló la conversión del archivo: {name}.{ext}\n')
            print_exc()
            print('')
    print('================================\n')

def images_string(extension: str, language_code: str) -> None:
    for i in seeker(('png', 'jpg', 'jpeg')):
        name, ext = i
        try:
            print(f'Convirtiendo el archivo a {name}.{ext} a {(extension).upper()}...')
            text = image_to_string(Image.open(f'{folder}{name}.{ext}'), lang=language_code, config='--psm 1')
            with open(f'{folder}{name}.{extension}', 'w+', encoding='utf-8') as file:
                file.write(text)
            print('Conversión del archivo exitosa!!\n')
        except:
            print(f'Falló la conversión del archivo: {name}.{ext}\n')
            print_exc()
            print('')
    print('================================\n')

def images_options() -> None:
    option = ' '
    while option not in ('1', '2', '3', '0'):
        option = input('CONVERTIR:\n\n1. a PNG\n2. a JPG\n3. a JPEG\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            converter_image('png')
        elif option == '2':
            converter_image('jpg')
        elif option == '3':
            converter_image('jpeg')

def images_string_options() -> None:
    option = ' '
    while option not in ('1', '2', '3', '4', '5', '6', '0'):
        option = input('SELECCIONE EL LENGUAJE DE LA IMAGEN POR FAVOR:\n\n1. English\n2. Español\t(Spanish)\n3. Français\t(French)\n4. Italiano\t(Italian)\n5. Pусский\t(Russian)\n6. Portugues\t(Portuguese)\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            images_string('txt', 'eng')
        elif option == '2':
            images_string('txt', 'spa')
        elif option == '3':
            images_string('txt', 'fra')
        elif option == '4':
            images_string('txt', 'ita')
        elif option == '5':
            images_string('txt', 'rus')
        elif option == '6':
            images_string('txt', 'por')