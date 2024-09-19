"""
Desarrollar  una función que  devuelva una subcadena  con  los últimos N  caracteres 
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
"""

def ultimos_caracteres(cadena: str, n: int):
    """
    Esta función retorna los ultimos N caracteres de una cadena.
    Recibe un string y un entero n, que determina los ultimos caracteres
    a buscar.
    Retorna una nueva cadena con los ultimos N caracteres.
    """
    print(len(cadena))
    print(n)
    if n > len(cadena):
        return cadena
    return cadena[-n:]


string = input("Ingrese la cadena: ")
posicion = int(input("Ingrese N: "))
salida = ultimos_caracteres(string, posicion)
print(f"Últimos {posicion} caracteres: '{salida}'")