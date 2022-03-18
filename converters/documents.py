from pdf2docx import parse
from docx2pdf import convert
from os import system

from helpers.seeker_file import seeker

def converter_document(ext, function):
    for i in seeker(ext):
        function(f'./conversor/{i}')

def documents_options():
    option = ' '
    while option not in ('1', '2'):
        option = input('CONVERTIR:\n\n1. De pdf a docx\n2. De docx a pdf\n\n0. Volver\n\n')
        system('cls')
        if option == '1':
            converter_document('pdf', parse)
        elif option == '2':
            converter_document('docx', convert)
