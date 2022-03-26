from os import system as s

from converters.audios import audios_options, audio_text_options
from converters.documents import documents_options
from converters.images import images_options, images_string_options
from converters.videos import videos_options, videos_audios_options

s('cls')
option = ''
while option != '0':
    option = input('QUE QUERES CONVERTIR?\n\n1. Audio\n2. Audio a Texto\n3. Documento\n4. Imagen\n5. Imagen a Texto\n6. Video\n7. Video a Audio\n\n0. Salir del programa\n\n')
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