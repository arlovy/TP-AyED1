"""
Eliminar de una lista de números enteros aquellos valores que se encuentren en 
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista 
resultante. La función debe modificar la lista original sin crear una copia modificada.
"""

def ingresar_numero_en_lista(numbers: list[int]):
    while True:
        ingresar = int(input("Ingrese un número (-1 para terminar): "))
        if ingresar != -1:
            numbers.append(ingresar)
        else:
            break


def borrar_valores(a: list[int], b: list[int]):
    for item in b:
        if item in a:
            veces = a.count(item)
            for _ in range(veces):
                a.remove(item)


def menu():
    """
    Esta opción ejecuta un menú para manejar el programa.
    No recibe ni retorna nada.
    """
    opciones = [
        "Cargar lista A",
        "Cargar lista B",
        "Eliminar valores de la lista B en la lista A",
        "Salir.",
    ]
    lista_a = []
    lista_b = []

    while True:
        for numero, opcion in enumerate(opciones):
            print(f"{numero + 1}. {opcion}")
        ingreso_opcion = int(input("Ingrese la opción: "))
        print()
        match ingreso_opcion:
            case 1:
                ingresar_numero_en_lista(lista_a)
                print()
                print(lista_a)
                print(lista_b)
                print()
            case 2:
                ingresar_numero_en_lista(lista_b)
                print()
                print(lista_a)
                print(lista_b)
                print()
            case 3:
                borrar_valores(lista_a, lista_b)
                print()
                print(lista_a)
                print(lista_b)
                print()
            case 4:
                print("Saliendo...")
                break


if __name__ == "__main__":
    menu()
