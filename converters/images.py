from PIL import Image
from os import system as s

from helpers.seeker_file import seeker, folder

def converter_image(extension_1: str, extension_2: str) -> None:
    for i in seeker(extension_1, extension_2):
        name, ext, ext2 = i
        img = Image.open(f"{folder}{name}.{ext}").convert('RGB')
        img.save(f'{folder}{name}.{ext2}')

def images_options():
    option = ' '
    while option not in ('1', '2', '3', '4', '0'):
        option = input('CONVERTIR:\n\n1. De PNG a JPG\n2. De PNG a JPEG\n3. De JPG a PNG\n4. De JPEG a PNG\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            converter_image('png', 'jpg')
        elif option == '2':
            converter_image('png', 'jpeg')
        elif option == '3':
            converter_image('jpg', 'png')
        elif option == '4':
            converter_image('jpeg', 'png')