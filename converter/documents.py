from os import system
from typing import Callable

from docx2pdf import convert
from pdf2docx import parse

from config import types
from helpers import file


def document(
        extension: str,
        extension2: str,
        function: Callable,
        message: bool = False) -> None:
    '''Convierte el/los archivo/s de documento a PDF o DOCX.'''
    for file_found in file.seeker(extension2):
        route, name, ext = file_found
        old_route = f'{route}.{ext}'

        if message:
            print(name)

        function(old_route)


def options() -> None:
    '''Elige la opción de conversión de documento.'''
    option = ' '
    while option not in types.documents:
        option = input(
            'CONVERTIR DOCUMENTO\n\n '
            '1. PDF a DOCX\n 2. DOCX a PDF\n\n0. Volver\n\n')
        system('cls')
    if option != '0':
        function = parse if option == '1' else convert
        file.decorator(
            document,
            extension=types.documents[option],
            extension2=types.documents2[option],
            function=function,
            message=True)
