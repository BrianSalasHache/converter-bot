from os import system

from converters.documents import documents_options
from converters.images import images_options

option = ''
while option != '0':
    system('cls')
    option = input('QUE QUERES CONVERTIR?\n\n1. Documento\n2. Imagen\n\n0. Salir del programa\n\n')
    system('cls')
    if option == '1':
        documents_options()
    elif option == '2':
        images_options()