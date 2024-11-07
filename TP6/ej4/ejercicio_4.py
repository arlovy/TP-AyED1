"""
Desarrollar un programa para eliminar todos los comentarios de un programa  es-
crito  en  lenguaje  Python.  Tener  en  cuenta  que  los  comentarios  comienzan  con  el 
signo # (siempre que éste no se encuentre encerrado entre comillas simples o do-
bles)  y  que  también  se  considera  comentario  a  las  cadenas  de  documentación 
(docstrings).
"""
import re

def eliminar_comentarios(ruta: str) -> None:
    '''
    Elimina comentarios y docstrings de un archivo específico.
    Recibe un string con la ruta del archivo.
    No retorna nada, modifica el archivo.
    '''

    with open(ruta, 'r', encoding='utf-8') as archivopy:
        codigo = archivopy.read()
        sin_comentarios = re.sub("(?m)\s*#.*$", "", codigo)
        sin_docstrings = re.sub("(?s)(\'\'\'(.*?)\'\'\'|\"\"\"(.*?)\"\"\")", "", sin_comentarios)
        with open(ruta, 'w', encoding='utf-8') as archivopy:
            archivopy.write(sin_docstrings.strip())


if __name__ == "__main__":
    RUTA = r"TP6\ej4\archivo.py"
    eliminar_comentarios(RUTA)