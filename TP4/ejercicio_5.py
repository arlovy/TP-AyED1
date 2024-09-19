"""
Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y 
un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres 
de la cadena original. 
Escribir también un programa para verificar el comportamiento de la misma. Hacer tres 
versiones de la función, para cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter
"""


def filtrar_palabras_ciclos(cadena: str, n: int):
    """
    Esta función recibe un string y un numero N, y retorna todas las palabras del string
    que tengan una longitud de N.
    Recibe un string y un entero positivo. 
    Retorna un string con todas las palabras de longitud N.
    """
    palabras = cadena.split()
    resultado = []

    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)

    return " ".join(resultado)


def filtrar_palabras_comprension(cadena: str, n: int):
    """
    Esta función recibe un string y un numero N, y retorna todas las palabras del string
    que tengan una longitud de N.
    Recibe un string y un entero positivo. 
    Retorna un string con todas las palabras de longitud N.
    """
    return ' '.join([palabra for palabra in frase.split() if len(cadena) >= n])


def filtrar_palabras_filter(cadena: str, n: int):
    """
    Esta función recibe un string y un numero N, y retorna todas las palabras del string
    que tengan una longitud de N.
    Recibe un string y un entero positivo. 
    Retorna un string con todas las palabras de longitud N.
    """
    return ' '.join(filter(lambda palabra: len(cadena) >= n, frase.split()))


if __name__ == "__main__":
    frase = input("Ingrese la frase: ")
    numero = int(input("Ingrese el valor de N: "))
    print(filtrar_palabras_ciclos(frase, numero))
    