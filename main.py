from os import system

from converters.audios import audios_options
from converters.documents import documents_options
from converters.images import images_options
from converters.videos import videos_options

option = ''
while option != '0':
    system('cls')
    option = input('QUE QUERES CONVERTIR?\n\n1. Audio\n2. Documento\n3. Imagen\n4. Videos\n\n0. Salir del programa\n\n')
    system('cls')
    if option == '1':
        audios_options()
    elif option == '2':
        documents_options()
    elif option == '3':
        images_options()
    elif option == '4':
        videos_options()