"""
Escribir una función que devuelva la suma de los N primeros números naturales.
"""


def sumatoria(numero: int) -> int:
    """
    Esta función genera la suma de todos los numeros de 1 a N.
    Recibe un número natural en formato entero.
    Retorna un entero.
    """
    if numero == 1:
        return 1
    return numero + sumatoria(numero - 1)

print(sumatoria(3))