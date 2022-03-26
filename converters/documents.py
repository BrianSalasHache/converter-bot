from pdf2docx import parse
from docx2pdf import convert
from typing import Callable
from traceback import print_exc
from os import system as s

from helpers.seeker_file import seeker, folder

def converter_document(extension: str, func: Callable) -> None:
    for file in seeker(extension):
        file = '.'.join(file)
        try:
            print(f'Convirtiendo el archivo {(file).upper()} ...')
            func(folder + file)
            print('Conversión del archivo exitosa!!\n')
        except:
            print(f'Falló la conversión del archivo: {file}\n')
            print_exc()
            print('')
    print('================================\n')

def documents_options() -> None:
    option = ' '
    while option not in ('1', '2', '0'):
        option = input('CONVERTIR:\n\n1. De pdf a docx\n2. De docx a pdf\n\n0. Volver\n\n')
        s('cls')
        if option == '1':
            converter_document('pdf', parse)
        elif option == '2':
            converter_document('docx', convert)