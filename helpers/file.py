import re

from datetime import datetime
from os import system
from pathlib import Path
from typing import List

folder = './conversor/'

def namer() -> str:
    while True:
        name = input('')
        system('cls')
        name = input('Caracteres especiales permitidos: "_", "-" y (espacio)\nElija el nombre del archivo:')
        if re.match('^[a-zA-Z 0-9ñ_-]*$', name):
            break
    if name == '':
        name = 'Grabacion ' + datetime.now().strftime('%d-%m-%Y %H-%M')
    return name

def seeker(ext1: str) -> List:
    route = list((Path.cwd() / folder).glob('*'))
    files = []
    for i in route:
        name, ext, file = i.stem, i.suffix.split('.')[1], i.name
        try:
            if ext in ext1:
                files.append([name, ext])
        except Exception as error:
            print(f'Falló la busqueda del archivo: {file}\nError: {error}')
    return files