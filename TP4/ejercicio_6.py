"""
Desarrollar una función que extraiga una subcadena de una cadena de caracteres, 
indicando  la  posición  y  la  cantidad  de  caracteres  deseada.  Devolver  la  subcadena 
como  valor  de  retorno.  Escribir  también  un  programa  para  verificar  el  comporta-
miento  de  la  misma.  Ejemplo,  dada  la  cadena  "El  número  de  teléfono  es  4356-
7890"  extraer  la  subcadena  que  comienza  en  la  posición  25  y  tiene  9  caracteres, 
resultando la subcadena "4356-7890". Escribir una función para cada uno de los si-
guientes casos:
    a. Utilizando rebanadas
    b. Sin utilizar rebanadas
"""


def extraer_subcadena_rebanada(cadena: str, posicion: int, cantidad: int):
    """
    Esta función recibe una cadena y retorna una parte específica de ella.
    Recibe una cadena, una posición y la cantidad de caracteres a partir
    de esa posición que se desea extraer.
    Retorna una nueva cadena.
    """
    return cadena[posicion:posicion + cantidad]


def extraer_subcadena_sin_rebanada(cadena: str, posicion: int, cantidad: int):
    """
    Esta función recibe una cadena y retorna una parte específica de ella.
    Recibe una cadena, una posición y la cantidad de caracteres a partir
    de esa posición que se desea extraer.
    Retorna una nueva cadena.
    """
    subcadena = ""

    for i in range(posicion, posicion + cantidad):
        if i < len(cadena):
            subcadena += cadena[i]

    return subcadena


if __name__ == "__main__":
    string = input("Ingrese el string: ")
    try:
        if string:
            posicion_inicial = int(input("Ingrese la posición inicial: "))
            caracteres = int(input("Ingrese la cantidad de caracteres a rebanar: "))
            salida1 = extraer_subcadena_rebanada(string, posicion_inicial, caracteres)
            salida2 = extraer_subcadena_sin_rebanada(string, posicion_inicial, caracteres)
            print(f"Subcadena extraída (con rebanadas): '{salida1}'")
            print(f"Subcadena extraida (sin rebanadas): '{salida2}'")
        else:
            print("El string está vacio.")
    except ValueError:
        print("Ingrese un entero.")
