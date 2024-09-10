"""
. Escribir funciones para:
    a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa 
    a través del teclado.

    b. Recibir una lista como parámetro y devolver True si la misma contiene algún 
    elemento repetido. La función no debe modificar la lista.

    c. Recibir una lista como parámetro y devolver una nueva lista con los elementos 
    únicos de la lista original, sin importar el orden. 

Combinar estas tres funciones en un mismo programa.
"""

import random as rn


def devolver_lista_unica(numbers: list[int]):
    """
    Esta función recibe una lista de enteros.
    Retorna la lista sin elementos repetidos, si tuviera alguno.
    """
    return list(set(numbers))


def hay_repetidos(numbers: list[int]):
    """
    Esta función recibe una lista de enteros.
    Retorna True o False segun si tiene elementos repetidos.
    """
    return len(numbers) == len(set(numbers))


def generar_lista(n: int):
    """
    Esta función recibe un entero N.
    Retorna una lista de N enteros aleatorios en el rango del 1 al 100.
    """
    return list(rn.randint(1, 100) for i in range(n))


def menu():
    """
    Esta opción ejecuta un menú para manejar el programa.
    No recibe ni retorna nada.
    """
    opciones = [
        "Generar lista de numeros aleatorios.",
        "Ver si la lista tiene elementos repetidos.",
        "Ver elementos unicos de la lista.",
        "Salir.",
    ]

    lista = []
    while True:
        for numero, opcion in enumerate(opciones):
            print(f"{numero + 1}. {opcion}")
        ingreso_opcion = int(input("Ingrese la opción: "))
        print()
        match ingreso_opcion:
            case 1:
                input_numeros = int(
                    input("Ingrese la cantidad de enteros que desea generar: ")
                )
                lista = generar_lista(input_numeros)
                print(lista)
                print()
            case 2:
                if hay_repetidos(lista):
                    print("Hay elementos repetidos en la lista.")
                else:
                    print("No hay elementos repetidos en la lista.")
                print()
            case 3:
                if lista:
                    lista_unica = devolver_lista_unica(lista)
                    print(lista_unica)
                else:
                    print("La lista generada está vacía.")
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida.\n")


if __name__ == "__main__":
    menu()
