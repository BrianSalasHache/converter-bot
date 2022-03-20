from pathlib import Path
from typing import List

folder = './conversor/'

def seeker(ext1: str, *args: str) -> List:
    route = list((Path.cwd() / folder).glob('*'))
    files = []
    for i in route:
        name, ext, file = i.stem, i.suffix, i.name
        if ext == f'.{ext1}' and not args:
            files.append(file)
        elif args and ext == f'.{ext1}':
            files.append([name, ext1, args[0]])
    return files