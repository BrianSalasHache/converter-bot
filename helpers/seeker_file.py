from pathlib import Path
from typing import List

folder = './conversor/'

def seeker(ext1: str, *args: str) -> List:
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