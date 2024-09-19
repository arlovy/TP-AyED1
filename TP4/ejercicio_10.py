"""
Desarrollar  una  función para  reemplazar  todas  las  apariciones  de  una  palabra  por 
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la 
cantidad de  reemplazos  realizados.  Tener  en  cuenta  que  sólo deben  reemplazarse 
palabras  completas,  y  no  fragmentos  de  palabras.  Escribir  también  un  programa 
para verificar el comportamiento de la función.
"""

import re

def reemplazar_palabra(cadena: str, palabra_a_reemplazar: str, nueva_palabra: str):
    patron = r'\b' + re.escape(palabra_a_reemplazar) + r'\b'

    nueva_cadena, cantidad_reemplazos = re.subn(patron, nueva_palabra, cadena)

    return nueva_cadena, cantidad_reemplazos


if __name__ == "__main__":
    string = input("Ingrese el string: ")
    reemplazar = input("Ingrese la palabra a reemplazar: ")
    nueva = input("Ingrese la nueva palabra: ")

    if string and reemplazar and nueva:
        if reemplazar in string.split():
            salida = reemplazar_palabra(string, reemplazar, nueva)
            print(f"La nueva palabra es {salida[0]}")
            print(f"Cantidad de reemplazos: {salida[1]}")
        else:
            print("La palabra a reemplazar no está en el texto.")
    else:
        print("Todos los strings deben tener texto.")
