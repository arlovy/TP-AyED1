"""
Resolver el siguiente problema, utilizando funciones:
    Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se 
    ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de car
    ga. Se solicita:

    a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe 
    aparecer una sola vez en el informe.
    b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus 
    ingresos. Mostrar los registros de entrada al club antes y después de 
    eliminarlo. Informar cuántos ingresos se eliminaron.
"""


def ingresar_socio(members: list[int]):
    """
    Solicita valores enteros y los appendea a una lista que recibe como parámetro.
    Finaliza cuando el usuario escribe 0.
    Recibe un lista, no retorna nada.
    """
    while True:
        input_usuario = int(
            input("Ingrese el número de socio (finalice carga con 0): ")
        )

        if input_usuario == 0:
            print("Saliendo...")
            break
        elif len(str(input_usuario)) != 5 or input_usuario < 0:
            print("Error. El número de socio debe tener 5 digitos positivos.")
        else:
            members.append(input_usuario)


def informar_veces_socio(members: list[int]):
    """
    Informa la cantidad de veces que aparece un valor dentro de una lista de enteros.
    Recibe como parámetro una lista de enteros.
    No retorna nada.
    """
    apariciones = ((item, members.count(item)) for item in set(members))
    for socio, veces in apariciones:
        print(f"El socio {socio} ha ingresado {veces} veces.")
    print()


def borrar_registros_socio(members: list[int], borrar: int):
    """
    Esta función borra todas las apariciones de un entero dentro de una lista de enteros.
    Recibe como parámetros una lista de enteros y un entero a borrar.
    No retorna nada.
    """
    for _ in range(members.count(borrar)):
        members.remove(borrar)


def menu():
    """
    Esta opción ejecuta un menú para manejar el programa.
    No recibe ni retorna nada.
    """
    opciones = [
        "Cargar socios",
        "Informar ingresos de socios",
        "Eliminar socio dado de baja",
        "Salir.",
    ]
    lista = []

    while True:
        for numero, opcion in enumerate(opciones):
            print(f"{numero + 1}. {opcion}")
        try:
            ingreso_opcion = int(input("Ingrese la opción: "))
            print()
            match ingreso_opcion:
                case 1:
                    ingresar_socio(lista)
                case 2:
                    informar_veces_socio(lista)
                case 3:
                    a_borrar = int(input("Ingrese el número de socio a borrar: "))
                    informar_veces_socio(lista)
                    borrar_registros_socio(lista, a_borrar)
                    informar_veces_socio(lista)
                case 4:
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no valida.")
        except ValueError:
            print("Error. Ingrese enteros.")


if __name__ == "__main__":
    menu()
