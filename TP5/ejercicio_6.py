"""
El método index permite buscar un elemento dentro de una lista, devolviendo la 
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se 
produce una excepción de tipo ValueError. Desarrollar un programa que cargue 
una lista con números enteros ingresados a través del teclado (terminando con -1) 
y permita que el usuario ingrese el valor de algunos elementos para visualizar la 
posición que ocupan, utilizando el método index. Si el número no pertenece a la 
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el 
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda
"""

def cargar_lista(listint: list[int]) -> None:
    """
    Solicita numeros enteros al usuario y los carga en una lista que recibe como parámetro.
    Recibe una lista de enteros.
    No retorna nada.
    """
    while True:
        try:
            n = int(input("Ingrese un número entero (-1 para finalizar): "))
            if n == -1:
                break
        except ValueError:
            print("\nError. El número ingresado no es un entero.")
        else:
            listint.append(n)


def buscar_en_lista(listint: list[int], search: int) -> None:
    """
    Esta función busca en una lista de enteros y printea la posición de un entero especificado.
    Recibe como parámetros una lista de enteros y un entero a buscar.
    No retorna nada.
    """
    try:
        print(f"El elemento indicado está en la posición {listint.index(search)}")
    except ValueError:
        print("\nError. El número ingresado no está en la lista.")


def menu():
    """
    Esta opción ejecuta un menú para manejar el programa.
    No recibe ni retorna nada.
    """
    opciones = [
        "Cargar elementos en la lista.",
        "Consultar por un elemento en la lista.",
        "Salir.",
    ]
    lista_enteros = []
    while True:
        for numero, opcion in enumerate(opciones):
            print(f"{numero + 1}. {opcion}")
        ingreso_opcion = int(input("Ingrese la opción: "))
        print()
        match ingreso_opcion:
            case 1:
                cargar_lista(lista_enteros)
                print(lista_enteros)
            case 2:
                intentos = 3
                while intentos > 0:
                    try:
                        n = int(input("Ingrese el número que desea buscar: "))
                    except ValueError:
                        print("\nError. Valor ingresado no válido.")
                        intentos -= 1
                    else:
                        buscar_en_lista(lista_enteros, n)
                if intentos == 0:
                    print("Abortando operación.\n")
            case 3:
                print("Saliendo...")
                break


if __name__ == "__main__":
    menu()
