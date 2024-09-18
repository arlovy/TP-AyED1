"""
Desarrollar cada una de las siguientes funciones y escribir un programa que permi
ta verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada fun
ción:
    a. Cargar números enteros en una matriz de N x N, ingresando los datos desde 
    teclado. 
    b. Ordenar en forma ascendente cada una de las filas de la matriz.
    c. Intercambiar dos filas, cuyos números se reciben como parámetro.
    d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
    e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
    f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
    parámetro.
    g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú
    mero se recibe como parámetro.
    h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
    i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
    j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo 
    una lista con los números de las mismas.
    NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera 
    sea el valor ingresado.
"""


def cargar_numeros(n: int):
    matrix = [
        [
            int(input(f"Ingrese el {j + 1}° entero de la {i + 1}° fila: "))
            for j in range(n)
        ]
        for i in range(n)
    ]
    return matrix


def ordenar_listas(matrix: list[list[int]]):
    for lista in matrix:
        lista.sort()


def intercambiar_filas(matrix: list[list[int]], c1: int, c2: int):
    aux = matrix[c1]
    matrix[c1] = matrix[c2]
    matrix[c2] = aux


def trasponer_matriz(matrix: list[list[int]]):
    return list(map(list, zip(*matrix)))


def calcular_promedios(matrix: list[list[int]], c: int):
    return sum(matrix[c]) / len(matrix[c])


def calcular_impares_percent(matrix: list[list[int]], c: int):
    impares = 0
    for numero in matrix[c]:
        if numero % 2 != 0:
            impares += 1
    return impares / len(matrix[c])


def xd():
    """
    Esta opción ejecuta un menú para manejar el programa.
    No recibe ni retorna nada.
    """
    opciones = [
        "Cargar una matriz de NxN",
        "Ordenar listas de manera ascendente",
        "Intercambiar filas de la matriz",
        "Trasponer matriz",
        "Calcular promedio de una fila",
        "Calcular porcentaje de elementos impares en una fila",
        "Determinar si la matriz es simétrica con respecto a su diagonal principal",
        "Determinar si la matriz es simétrica con respecto a su diagonal secundaria",
        "Determinar qué columnas de la matriz son palíndromos (capicúas)",
        "Salir.",
    ]
    matriz = []
    while True:
        for numero, opcion in enumerate(opciones):
            print(f"{numero + 1}. {opcion}")
        ingreso_opcion = int(input("Ingrese la opción: "))
        print()
        match ingreso_opcion:
            case 1:
                while True:
                    try:
                        user_input = int(input("Ingrese N: "))
                        matriz = cargar_numeros(user_input)
                        print(matriz)
                        print()
                        break
                    except ValueError:
                        print("El valor ingresado no es válido. Intente nuevamente. \n")
            case 2:
                if matriz:
                    ordenar_listas(matriz)
                    print(matriz)
                else:
                    print("La matriz está vacia.")
            case 3:
                if matriz:
                    col1 = int(input("Ingrese el indice de la columna A: "))
                    col2 = int(input("Ingrese el indice de la columna B: "))
                    intercambiar_filas(matriz, col1, col2)
                    print(matriz)
                    print()
                else:
                    print("La matriz está vacia.")
            case 4:
                if matriz:
                    matriz = trasponer_matriz(matriz)
                else:
                    print("La matriz está vacía.")
            case 5:
                if matriz:
                    columna = int(input("Ingrese la columna: "))
                    salida = calcular_promedios(matriz, columna)
                    print(f"El promedio de la columna {columna} es {salida}")
                else:
                    print("La matriz está vacia.")
            case 6:
                if matriz:
                    columna = int(input("Ingrese la columna: "))
                    porcentaje = calcular_impares_percent(matriz, columna)
                    print(
                        f"{porcentaje}% de los valores de la columna {columna} son impares."
                    )
                    print()
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                print("Saliendo...")
                break
            case _:
                print("Opción no válida.")


if __name__ == "__main__":
    xd()
