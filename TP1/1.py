"""
Desarrollar una función que reciba tres números enteros positivos y devuelva el 
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en 
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar 
también un programa para ingresar los tres valores, invocar a la función y mostrar 
el máximo hallado, o un mensaje informativo si éste no existe.
"""


def comparar_enteros(lista_enteros):
    maximo_entero = max(lista_enteros)
    if lista_enteros.count(maximo_entero) > 1:
        return "No hay un mayor estricto"
    return f"El mayor valor es {maximo_entero}"


if __name__ == "__main__":

    enteros = [int(input(f"Ingrese el {i + 1}° entero: ")) for i in range(3)]
    no_hay_negativos = True
    for entero in enteros:
        if entero < 0:
            print("Error. Todos los enteros deben ser positivos.")
            no_hay_negativos = False
            break
    if no_hay_negativos:
        print(comparar_enteros(enteros))