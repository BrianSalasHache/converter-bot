from os import system

from colorama import Fore, Style
import colorama

from helpers import open
from config import options


open.folder()
colorama.init(autoreset=True)


system('cls')
option = ''
while option != '0':
    print(f'{Fore.CYAN}{Style.BRIGHT}|> CONVERTER - BOT <|\n ')
    option = input(' '
                   '1. Convertir Audio\n 2. Convertir Documento\n '
                   '3. Convertir Imagen\n 4. Convertir Video\n 5. Grabar\n '
                   '6. Leer\n 7. Traducir\n\n0. Salir del programa\n\n')
    system('cls')
    if option in options.main:
        options.main[option]()
