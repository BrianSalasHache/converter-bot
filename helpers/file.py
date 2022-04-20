from datetime import datetime
from os import system
from pathlib import Path
from typing import Callable, List, Tuple
import re


folder = './conversor/'


def decorator(
        func: Callable,
        sym: str = '=',
        msg: str = 'Convirtiendo a',
        *args,
        **kwargs) -> None:
    '''Decora las funciones conversoras para mostrar el progreso.'''
    if msg != '':
        if 'extension' in kwargs:
            ext = kwargs['extension'].upper()
            print(f'{msg} {ext}...\n')
        else:
            print(f'{msg}...\n')
    func(*args, **kwargs)
    print('\nSe finalizó con éxito!!')
    print(f'{sym*40}\n')


def namer() -> Tuple[str, str]:
    '''Nombra los archivos de salida.

    Pide un nombre a el usuario y lo guarda.
    En el caso de que el usuario no escriba nada,
    el nombre se guarda usando datetime.
    '''
    while True:
        name = input('')
        system('cls')
        name = input(
            'Caracteres especiales permitidos: "_", "-" y (espacio)\n'
            'Elija el nombre del archivo:')
        if re.match('^[a-zA-Z 0-9ñ_-]*$', name):
            break
    if name == '':
        name = 'Grabacion ' + datetime.now().strftime('%d-%m-%Y %H-%M')
    return folder + name, name


def seeker(ext1: str) -> List:
    '''Busca los archivos dentro de la carpeta "conversor".
    Una vez encontrados los guarda en una lista.
    '''
    route = list((Path.cwd() / folder).glob('*'))
    files = []
    for i in route:
        name, ext, file = i.stem, i.suffix.split('.')[1], i.name
        try:
            if ext in ext1:
                files.append([folder + name, name, ext])
        except Exception as error:
            print(f'Falló la busqueda del archivo: {file}\nError: {error}')
    return files
