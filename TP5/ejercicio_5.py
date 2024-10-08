"""
La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del 
módulo math. Escribir un programa que utilice esta función para calcular la raíz 
cuadrada de un número cualquiera ingresado a través del teclado. El programa 
debe utilizar manejo de excepciones para evitar errores si se ingresa un número 
negativo
"""
from math import sqrt

def raiz_cuadrada(num:int) -> float:
    """
    Calcula la raíz cuadrada de un número X y retorna
    -1.0 si se le pasa como número un negativo.
    Recibe como parámetro un número entero.
    Retorna un float.
    """
    try:
        assert num > 0
        return sqrt(num)
    except AssertionError:
        return -1.0

if __name__ == "__main__":
    try:
        n = float(input("Ingrese el número para ver su raíz cuadrada: "))
        salida = raiz_cuadrada(n)
        if salida != -1.0:
            print(salida)
        else:
            print("No se puede calcular la raíz cuadrada de un negativo.")
    except ValueError:
        print("El número ingresado no es válido.")
