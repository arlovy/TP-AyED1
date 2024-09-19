"""
Escribir una función que reciba como parámetro una cadena de caracteres en la que 
las  palabras  se  encuentran  separadas  por  uno  o  más  espacios.  Devolver  otra 
cadena  con  las  palabras  ordenadas  según  su  longitud,  dejando  un  espacio  entre 
cada  una.  Los  signos  de  puntuación  no  deben  ser  tenidos  en  cuenta  al  medir  la 
longitud de las palabras, pero deberán conservarse en la cadena final.
"""

def ordenar_longitud(string: str):
    """
    Esta función ordena las palabras de una cadena por longitud.
    Recibe una cadena no vacía.
    Retorna la cadena con las palabras ordenadas por longitud.
    """
    assert len(string) > 0

    palabras = string.split()

    def longitud_sin_puntuacion(palabra):
        palabra_limpia = ''.join([char for char in palabra if char not in [".",",",";"]])
        return len(palabra_limpia)

    palabras_ordenadas = sorted(palabras, key=longitud_sin_puntuacion)

    return ' '.join(palabras_ordenadas)

ingreso_cadena = input("Ingrese la cadena: ")
print(ordenar_longitud(ingreso_cadena))
