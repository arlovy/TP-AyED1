"""
Realizar  una  función  recursiva  para  imprimir  una  matriz  de  M  x  N  con  el  formato 
apropiado.
"""

def mostrar_matriz(matriz: list[list[int]], inicio:int=0) -> None:
    """
    Printea una matriz.
    Recibe una matriz de enteros y un entero valor de inicio que representa la fila actual.
    No retorna nada.
    """
    if not matriz:
        raise ValueError("La matriz proporcionada no tiene valores.")
    if inicio == len(matriz):
        return None
    print(" ".join(str(n) for n in matriz[inicio]))
    return mostrar_matriz(matriz, inicio+1)

mostrar_matriz([[1,3,2],[2,5,4]])