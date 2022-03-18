from os import system

from converters.documents import documents_options

option = ''
while option != '0':
    system('cls')
    option = input('QUE QUERES CONVERTIR?\n\n1. Documento\n\n0. Salir del programa\n\n')
    system('cls')
    if option == '1':
        documents_options()