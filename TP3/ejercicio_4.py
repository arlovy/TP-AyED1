"""
Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas 
en cada una de sus plantas durante una semana. De este modo, cada columna re-
presenta el día de la semana y cada fila a una de sus fábricas. Ejemplo: (Ver pdf)

    a. Crear una matriz con datos generados al azar para N fábricas durante una 
    semana,  considerando  que  la  capacidad  máxima  de  fabricación  es  de  150 
    unidades  por  día  y  puede  suceder  que  en  ciertos  días  no  se  fabrique  nin-
    guna. 
    b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica. 
    c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
    d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
    e. Crear una lista por comprensión que contenga la menor cantidad fabricada 
    por cada fábrica.
"""

import random as rn


def total_fabricado(matrix: list[list[int]]) -> list[int]:
    """
    Retorna la suma de todos los elementos dentro de cada fila de una matriz.
    Recibe una matriz de enteros.
    Retorna una lista de enteros.
    """
    return [sum(x) for x in matrix]


def imprimir_resultado(matrix: list[list[int]], n_total: list[int]) -> None:
    """
    Printea la producción de la semana para cada una de las fábricas junto al
    total producido.
    Recibe una matriz de enteros, y una lista de enteros con la producción
    total de cada fábrica.
    No retorna nada.
    """
    resultados = "\n"
    for i, produccion in enumerate(matrix, start=1):
        resultados += f"Fabrica {i}: {produccion}\nTOTAL: {n_total[i - 1]}\n"
    print(resultados)


def mayor_prod_dia(matrix: list[list[int]]) -> tuple[int, int]:
    """
    Itera la matriz y busca el día con la mayor producción.
    Recibe una matriz de enteros.
    Retorna una tupla (dia con mayor prod, indice de fabrica)
    """
    produccion_max = max([max(x) for x in matrix])
    for fab in matrix:
        for day in fab:
            if day == produccion_max:
                salida = (fab.index(day), matrix.index(fab))
    return salida


def dia_mas_productivo(matrix: list[list[int]]) -> int:
    """
    Suma la producción de todas las fábricas para cada dia de la semana
    y retorna el día donde más se ha producido entre todas las fábricas.
    Recibe una matriz de enteros.
    Retorna un entero.
    """
    produccion_dias = [sum([fabrica[dia] for fabrica in matrix]) for dia in dias]
    dia_max = produccion_dias.index(max(produccion_dias))
    return dia_max


def menor_cant_fabrica(matrix: list[list[int]]) -> list[int]:
    """
    Crea una lista con la menor producción de cada fábrica en la semana.
    Recibe una matriz de enteros.
    Retorna una lista de enteros.
    """
    return [min(fabrica) for fabrica in matrix]


if __name__ == "__main__":
    dias = {
        0: "Lunes",
        1: "Martes",
        2: "Miercoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sabado",
    }

    matriz = []

    try:
        n = int(input("Ingrese la cantidad de fabricas: "))
        if n < 0:
            print("El numero debe ser positivo.")
        else:
            matriz = [[rn.randint(0, 150) for _ in range(len(dias))] for _ in range(n)]
    except ValueError:
        print("Debe ingresar un numero.")

    if matriz:
        total = total_fabricado(matriz)
        imprimir_resultado(matriz, total)
        dia, fabrica = mayor_prod_dia(matriz)
        print(
            f"La fábrica {fabrica + 1} fue la que más produjo, el día {dias.get(dia)}."
        )
        day_max = dia_mas_productivo(matriz)
        print(f"El día mas productivo fue el {dias.get(day_max)}.")
