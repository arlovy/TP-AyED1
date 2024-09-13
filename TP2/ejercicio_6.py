"""
Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas 
que cada elemento tiene en la lista original.
Desarrollar también un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""

def normalize(numbers: list[int]) -> list[int]:
    """
    Esta función recibe como parámetros una lista de enteros, y retorna
    una lista normalizada correspondiente a ella.
    """
    total = sum(numbers)
    return [num/total for num in numbers]


def menu():
    """
    Esta opción ejecuta un menú para manejar el programa.
    No recibe ni retorna nada.
    """
    opciones = [
        "Cargar lista de enteros y normalizar.",
        "Salir.",
    ]

    while True:
        numeros = []
        for numero, opcion in enumerate(opciones):
            print(f"{numero + 1}. {opcion}")
        ingreso_opcion = int(input("Ingrese la opción: "))
        print()
        match ingreso_opcion:
            case 1:
                user_input = 0
                while user_input != -1:
                    try:
                        user_input = int(input("Ingrese el número (-1 para finalizar): "))
                        if user_input < -1:
                            print("Los datos ingresados deben ser positivos.")
                        else:
                            if user_input != -1:
                                numeros.append(user_input) 
                            else:
                                print(f"Tu lista: \n{numeros}")
                                print(f"Lista normalizada: \n {normalize(numeros)}\n")
                    except:
                        print("El dato ingresado no es válido.")
                        continue
 
            case 2:
                print("Saliendo...")
                break
            case _:
                print("Opción no válida.")


if __name__ == "__main__":
    menu()