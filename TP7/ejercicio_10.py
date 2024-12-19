"""
Escribir una  función que  sume  todos los  elementos de una  matriz de  M  x  N  y de-
vuelva el resultado. No usar la función sum().
"""

def sumar_matriz(matriz: list[list[int]], fila:int=0, column:int=0) -> int:
    """
    Suma todos los valores dentro una matriz.
    Recibe una matriz de enteros y dos enteros que representan la fila y columna actual.

    Post: Returns the sum of the matrix, an integer.

    Raises: ValueError: if m is empty.

    """
    if not matriz:
        raise ValueError("La matriz esta vacia.")
    if fila == len(matriz):
        return 0
    if column == len(matriz[fila]):
        return sumar_matriz(matriz, fila + 1, 0)
    return matriz[fila][column] + sumar_matriz(matriz, fila, column + 1)

print(sumar_matriz([[1,3,2],[3,3]]))
