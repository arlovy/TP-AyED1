"""
Desarrollar una función que reciba tres números enteros positivos y devuelva el 
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en 
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar 
también un programa para ingresar los tres valores, invocar a la función y mostrar 
el máximo hallado, o un mensaje informativo si éste no existe.
"""

def comparar_enteros(a,b,c):
    lista_enteros = [a,b,c]
    maximo_entero = max(lista_enteros)
    if lista_enteros.count(maximo_entero) > 1:
        return "No hay un mayor estricto"
    return f"El mayor valor es {maximo_entero}"


if __name__ == "__main__":
    int1 = int(input("Ingrese el primer entero: "))
    int2 = int(input("Ingrese el segundo entero: "))
    int3 = int(input("Ingrese el tercer entero: "))
    print(comparar_enteros(int1,int2,int3))