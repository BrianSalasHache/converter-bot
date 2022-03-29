from os import system as s

from converters.audios import audios_options
from converters.documents import documents_options
from converters.images import images_options
from converters.recorder import recorder_options
from converters.translator import translator_options
from converters.videos import videos_options

s('cls')
option = ''
while option != '0':
    option = input('CONVERTER-BOT\n\n 1. Convertir Audio\n 2. Convertir Documento\n 3. Convertir Imagen\n 4. Convertir Video\n 5. Convertir Grabación\n 6. Traducir\n\n0. Salir del programa\n\n')
    s('cls')
    if option == '1':
        audios_options()
    elif option == '2':
        documents_options()
    elif option == '3':
        images_options()
    elif option == '4':
        videos_options()
    elif option == '5':
        recorder_options()
    elif option == '6':
        translator_options()