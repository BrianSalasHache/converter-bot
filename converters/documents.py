from pdf2docx import parse
from docx2pdf import convert
from os import system
from typing import Callable

from helpers.seeker_file import seeker, folder

def converter_document(ext: str, func: Callable) -> None:
    for file in seeker(ext):
        func(folder + file)

def documents_options() -> None:
    option = ' '
    while option not in ('1', '2'):
        option = input('CONVERTIR:\n\n1. De pdf a docx\n2. De docx a pdf\n\n0. Volver\n\n')
        system('cls')
        if option == '1':
            converter_document('pdf', parse)
        elif option == '2':
            converter_document('docx', convert)