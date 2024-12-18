"""
Realizar una función que devuelva el resto de dos números enteros, utilizando res-
tas sucesivas.
"""

def calcular_resto(n1: int, n2: int) -> int:
    """
    Calcula el resto de una división de forma recursiva.
    Recibe dos enteros positivos, siendo N1 el dividendo y N2 el divisor.
    Retorna el resto de la división n1//n2.
    """
    if 0 in (n1,n2): #jijazo
        raise ValueError("División por cero.")
    if n1 < 0 or n2 < 0:
        raise ValueError("Los parámetros pasados deben ser positivos.")
    if n2 > n1: #retorna el resto si no se pudiera restar mas
        return n1
    if n1 == n2:
        return 0
    return calcular_resto(n1 - n2, n2)