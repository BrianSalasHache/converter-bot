from os import system

from converter import audios, documents, images, reader, recorder, translator, videos

system('cls')
option = ''
while option != '0':
    option = input('CONVERTER-BOT\n\n 1. Convertir Audio\n 2. Convertir Documento\n 3. Convertir Imagen\n 4. Convertir Video\n 5. Grabar\n 6. Leer\n 7. Traducir\n\n0. Salir del programa\n\n')
    system('cls')
    if option == '1':
        audios.options()
    elif option == '2':
        documents.options()
    elif option == '3':
        images.options()
    elif option == '4':
        videos.options()
    elif option == '5':
        recorder.options()
    elif option == '6':
        reader.options()
    elif option == '7':
        translator.options()