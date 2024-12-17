"""
Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas.
"""

def producto(n1: int, n2: int) -> int:
    """
    Calcula el producto entre dos números usando sumas sucesivas.
    Recibe dos enteros, el primero es el número a sumar y el segundo la cantidad de veces que se suma.
    Retorna el producto entre los dos números.
    """
    if n2 == 0:
        return 0
    return n1 + producto(n1, n2 - 1)
