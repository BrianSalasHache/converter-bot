from os import path
import webbrowser


def folder() -> None:
    '''Abre una carpeta del escritorio en el explorador.

    Para ser exactos abre la carpeta "conversor"
    '''
    RUTA_CARPETA = "./conversor"
    webbrowser.open(path.realpath(RUTA_CARPETA))
