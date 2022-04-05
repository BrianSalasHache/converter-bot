from gtts import gTTS
from os import system, remove

from config import languages, types
from converter import images
from helpers import file

def reader(language: str, domain: str, delete: bool):
    for file_found in file.seeker('txt'):
        name, ext = file_found
        print(f'Convirtiendo el archivo a {name}.{ext} a MP3...')
        text = open(f'{file.folder}{name}.{ext}', 'r', encoding='utf-8').read()
        speech = gTTS(text=text, lang=language, tld=domain, slow=False)
        speech.save(f'{file.folder}{name}-reader-{language}-{domain}.mp3')
        print('Conversión del archivo exitosa!!\n')
        if delete:
            remove(f'{file.folder}{name}.{ext}')
    print('================================\n')

def language(delete: bool = False) -> None:
    option = ' '
    while option not in (languages.reader):
        option = input('SELECCIONE EL LENGUAJE DEL LECTOR:\n\n1. English\t(United Kingdom)\n2. English\t(United States)\n3. Español\t(Mexico)\n4. Español\t(España)\n5. Français\t(France)\n6. Portugues\t(Brazil)\n7. Portugues\t(Portugal)\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        language, domain = languages.reader[option]
        reader(language, domain, delete)

def options() -> None:
    option = ' '
    while option not in (types.reader):
        option = input('LEER\n\n 1. Imagen\n 2. Texto\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        if option == '1' and images.language() == True:
            language(True)
        elif option == '2': 
            language()