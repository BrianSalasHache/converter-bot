from docx2pdf import convert
from pdf2docx import parse
from typing import Callable
from os import system

from config import types
from helpers import file

def document(extension: str, func: Callable) -> None:
    for file_found in file.seeker(extension):
        file_found = '.'.join(file_found)
        print(f'Convirtiendo el archivo {(file_found).upper()} ...')
        func(file.folder + file_found)
        print('Conversión del archivo exitosa!!\n')
    print('================================\n')

def options() -> None:
    option = ' '
    while option not in (types.documents):
        option = input('CONVERTIR DOCUMENTO\n\n 1. PDF a DOCX\n 2. DOCX a PDF\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        document(types.documents[option], parse if option == '1' else convert)