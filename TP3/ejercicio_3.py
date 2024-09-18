"""
Desarrollar un programa para rellenar una matriz de N x N con números enteros al 
azar comprendidos en el intervalo [0,N**2), de tal forma que ningún número se repi-
ta. Imprimir la matriz por pantalla.
"""

import random as rn


def llenar_matriz(n: int) -> list:
    """
    Esta función retorna una matriz de NxN con números unicos en el
    intervalo [0, N**2).
    Recibe un numero entero positivo.
    Retorna una matriz.
    """
    numbers = list(set(i for i in range(n**2)))
    print(numbers)
    matriz = []
    for i in range(n):
        row = []
        for _ in range(n):
            num = rn.choice(numbers)
            row.append(num)
            numbers.remove(num)
        print(row)
        matriz.append(row)
    return matriz


ingresar = int(input("Ingrese N: "))
salida = llenar_matriz(ingresar)
print(salida)
