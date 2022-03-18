from PIL import Image
from os import system

from helpers.seeker_file import seeker

def converter_image(ext1, ext2):
    for i in seeker(ext1, ext2):
        img = Image.open(f"./conversor/{i[0]}.{i[1]}")
        rgb_im = img.convert('RGB')
        rgb_im.save(f'./conversor/{i[0]}.{i[2]}')

def images_options():
    option = ' '
    while option not in ('1', '2', '3', '4', '0'):
        option = input('CONVERTIR:\n\n1. De PNG a JPG\n2. De PNG a JPEG\n3. De JPG a PNG\n4. De JPEG a PNG\n\n0. Volver\n\n')
        system('cls')

        if option == '1':
            converter_image('png', 'jpg')
        elif option == '2':
            converter_image('png', 'jpeg')
        elif option == '3':
            converter_image('jpg', 'png')
        elif option == '4':
            converter_image('jpeg', 'png')