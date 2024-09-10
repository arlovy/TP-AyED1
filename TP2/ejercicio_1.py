"""
Desarrollar cada una de las siguientes funciones y escribir un programa que per
mita verificar su funcionamiento imprimiendo la lista luego de invocar a cada fun
ción:
    a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elemen
    tos también será un número al azar de dos dígitos.

    b. Calcular y devolver el producto de todos los elementos de la lista anterior.

    c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar 
    se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar 
    listas auxiliares.

    d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas 
    auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]
"""

import random as rn
from functools import reduce


def generar_lista():
    """
    Esta función genera una lista con una cantidad al azar de números de cuatro dígitos aleatorios.
    No recibe nada, y retorna una lista de enteros.
    """
    return list(rn.randint(1000, 9999) for i in range(rn.randint(10, 99)))


def calcular_productos(numbers: list[int]):
    """
    Recibe una lista de enteros y retorna el producto de todos los enteros dentro de la lista.
    Si está vacía, retorna -1.
    """
    if numbers:
        return reduce(lambda x, y: x * y, numbers)
    else:
        return -1


def borrar_valor(numbers: list[int], target: int):
    """
    Recibe como parámetros una lista de enteros, y un entero a borrar.
    Busca todas las apariciones de el entero en la lista, y lo elimina.
    """
    veces = numbers.count(target)
    for _ in range(veces):
        numbers.remove(target)


def es_capicua(numbers: list[int]):
    """
    Recibe una lista de enteros.
    Retorna True si la lista es capicúa.
    Retorna False si no lo es, o si la lista está vacía.
    """
    if numbers:
        for i in range(len(numbers) // 2):
            if numbers[i] != numbers[len(numbers) - i - 1]:
                return False
        return True
    else:
        return False


def menu():
    """
    Esta opción ejecuta un menú para manejar el programa.
    No recibe ni retorna nada.
    """
    opciones = [
        "Generar una lista al azar.",
        "Calcular producto de los elementos de la lista.",
        "Borrar un valor de la lista.",
        "Ver si la lista es capicúa.",
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
                lista = generar_lista()
                print(lista)
                print()
            case 2:
                productos = calcular_productos(lista)
                if productos == -1:
                    print("No hay elementos en la lista.\n")
                else:
                    print(productos)
                    print()
            case 3:
                a_borrar = int(input("Ingrese el entero a borrar: "))
                if a_borrar in lista:
                    borrar_valor(lista, a_borrar)
                    print(lista)
                else:
                    print("El número indicado no está en la lista.\n")
            case 4:
                if es_capicua(lista):
                    print("La lista es capicúa.")
                else:
                    print("La lista no es capicúa.")
                print()
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida.\n")


if __name__ == "__main__":
    menu()
