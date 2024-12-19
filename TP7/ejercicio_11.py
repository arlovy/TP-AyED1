"""
Desarrollar una función que devuelva el mínimo elemento de una matriz de M x N.
"""

def minimo_matriz(matriz: list[list[int]], fila:int=0, column:int=0, minimo:int=None) -> int:
    """
    Encuentraa el valor mínimo dentro de una matriz de enteros.
    Recibe una matriz de enteros, la fila actual, la columna actual y el valor mínimo que por
    defecto es None.
    Retorna el mínimo.
    """
    if not matriz:
        raise ValueError("La matriz no tiene valores.")

    if minimo is None:
        minimo = matriz[0][0]

    if fila == len(matriz):
        return minimo

    if column == len(matriz[fila]):
        return minimo_matriz(matriz, fila + 1, 0, minimo)

    minimo = min(minimo, matriz[fila][column])
    return minimo_matriz(matriz, fila, column + 1, minimo)

print(minimo_matriz([[1,5,6],[-2,4,2]]))