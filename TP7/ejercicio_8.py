"""
Realizar la implementación recursiva del método de selección para ordenar una lista 
de números  enteros.  Sugerencia: Colocar  el elemento más pequeño  en la primera 
posición, y luego ordenar el resto de la lista con una llamada recursiva. No usar las 
funciones min() ni max() de Python.
"""

def ordenar_lista(n: list[int], inicio:int = 0) -> list[int]:
    """
    Ordena una lista de manera ascendente.
    Recibe una lista de enteros y un entero que indica la posición de inicio.
    Retorna la lista ordenada.
    """
    if not n:
        raise ValueError("No hay valores en la lista.")
    if inicio == len(n) - 1:
        return n

    minimo = inicio
    for item, elem in enumerate(n[inicio + 1:], start=inicio + 1):
        if elem < n[minimo]:
            minimo = item
    n[inicio], n[minimo] = n[minimo], n[inicio]
    return ordenar_lista(n, inicio + 1)

print(ordenar_lista([1,2,6,7,3,2,5,6]))
