"""
Desarrollar una función que reciba tres números enteros positivos y devuelva el 
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en 
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar 
también un programa para ingresar los tres valores, invocar a la función y mostrar 
el máximo hallado, o un mensaje informativo si éste no existe.
"""


def comparar_enteros(lista_enteros):
    """
    Esta función verifica si existe un número mayor estricto en
    una lista de números.

    La función recibe una lista de enteros.
    Retorna el mayor estricto. Si no existiera, retorna False.
    """
    maximo_entero = max(lista_enteros)
    if lista_enteros.count(maximo_entero) > 1:
        return -1
    return maximo_entero


def verificar_positivos(lista_enteros):
    """
    Verifica que todos los números en una lista sean positivos.

    Recibe una lista de enteros.
    Retorna True si todos los elementos son positivos.
    Si encuentra un elemento negativo, retorna False.
    """
    for numero in lista_enteros:
        if numero < 0:
            return False
    return True


if __name__ == "__main__":

    try:
        enteros = [int(input(f"Ingrese el {i + 1}° entero: ")) for i in range(3)]
        MAYOR_ESTRICTO = comparar_enteros(enteros)
        if verificar_positivos(enteros):
            print(f"El mayor estricto es {MAYOR_ESTRICTO}")
        else:
            print("Todos los números deben ser positivos.")

    except ValueError:
        print("Error. Todos los datos deben ser enteros.")
