"""
    Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), 
    donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valo
    res de la lista.
"""


def generar_lista(n: int):
    """
    Esta función recube un entero N y retorna una lista con todos los cuadrados desde 1 hasta N.
    """
    return list(i**2 for i in range(1, n + 1))


def printear_ultimos(lista: list):
    """
    Printea los 10 últimos elementos de una lista.
    """
    print(lista[-10:])


def menu():
    """
    Esta opción ejecuta un menú para manejar el programa.
    No recibe ni retorna nada.
    """
    opciones = [
        "Generar lista de cuadrados y ver los 10 últimos.",
        "Salir.",
    ]

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
                printear_ultimos(lista)
                print()
            case 2:
                print("Saliendo...")
                break


if __name__ == "__main__":
    menu()
