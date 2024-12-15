"""
Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
utilizar cadenas de caracteres.
"""

def cantidad_de_digitos(n: int) -> int:
    """
    Calcula recursivamente la cantidad de dígitos que posee un número N.
    Recibe un entero N.
    Retorna la cantidad de dígitos del número.
    """
    if n == 0 or (n < 10 and n > -10):
        return 1
    return 1 + cantidad_de_digitos(n // 10)
