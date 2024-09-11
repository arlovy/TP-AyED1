"""
    Escribir una función que reciba una lista como parámetro y devuelva True si la lista 
    está ordenada en forma ascendente o False en caso contrario. Por ejemplo, 
    ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar 
    además un programa para verificar el comportamiento de la función.
"""

def es_ascendente(numbers: list[int]):
    """
    Recibe una lista de enteros y retorna True o False según si los elementos dentro de
    ella están ordenados de manera ascendente.
    """
    assert len(numbers) > 1
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))


if __name__ == "__main__":
    lista_loca = [1]
    print(es_ascendente(lista_loca))