from os import system as s

from converters.audios import audios_options, audio_text_options
from converters.documents import documents_options
from converters.images import images_options, images_string_options
from converters.videos import videos_options, videos_audios_options
from converters.translator import translator_options
s('cls')
option = ''
while option != '0':
    option = input('QUE QUERES HACER?\n\n1. Convertir Audio\n2. Convertir Audio a Texto\n3. Convertir Documento\n4. Convertir Imagen\n5. Convertir Imagen a Texto\n6. Convertir Video\n7. Convertir Video a Audio\n8. Traducir un Texto\n9. Traducir una Imagen\n\n0. Salir del programa\n\n')
    s('cls')
    if option == '1':
        audios_options()
    elif option == '2':
        audio_text_options()
    elif option == '3':
        documents_options()
    elif option == '4':
        images_options()
    elif option == '5':
        images_string_options()
    elif option == '6':
        videos_options()
    elif option == '7':
        videos_audios_options()
    elif option == '8':
        translator_options(0)
    elif option == '9':
        images_string_options()
        translator_options(1)