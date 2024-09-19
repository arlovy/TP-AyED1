"""
Escribir  una  función  para  eliminar  una  subcadena  de  una  cadena  de  caracteres,  a 
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resul-
tante. Escribir también un programa para verificar el comportamiento de la misma. 
Escribir una función para cada uno de los siguientes casos:
    a. Utilizando rebanadas
    b. Sin utilizar rebanadas
"""


def eliminar_subcadena_rebanada(cadena: int, posicion: int, cantidad: int):
    """
    Esta función elimina una sección de una cadena.
    Recibe una cadena, un entero que determina la posición inicial, y una
    cantidad de caracteres a eliminar.
    Retorna una nueva cadena.
    """
    return cadena[:posicion] + cadena[posicion + cantidad :]


def eliminar_subcadena_sin_rebanada(cadena: int, posicion: int, cantidad: int):
    """
    Esta función elimina una sección de una cadena.
    Recibe una cadena, un entero que determina la posición inicial, y una
    cantidad de caracteres a eliminar.
    Retorna una nueva cadena.
    """
    nueva_cadena = ""

    for i in range(len(cadena)):
        if i < posicion or i >= posicion + cantidad:
            nueva_cadena += cadena[i]

    return nueva_cadena


if __name__ == "__main__":
    string = input("Ingrese el string: ")
    try:
        if string:
            posicion_inicial = int(input("Ingrese la posición inicial: "))
            caracteres = int(input("Ingrese la cantidad de caracteres a rebanar: "))
            salida1 = eliminar_subcadena_rebanada(string, posicion_inicial, caracteres)
            salida2 = eliminar_subcadena_sin_rebanada(
                string, posicion_inicial, caracteres
            )
            print(f"Subcadena extraída (con rebanadas): '{salida1}'")
            print(f"Subcadena extraida (sin rebanadas): '{salida2}'")
        else:
            print("El string está vacio.")
    except ValueError:
        print("Ingrese un entero.")
