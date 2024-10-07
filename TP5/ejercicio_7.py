"""
Escribir un programa que juegue con el usuario a adivinar un número. El programa 
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para 
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el nú
mero que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga 
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar 
el número. Si el usuario introduce algo que no sea un número se mostrará un 
mensaje en pantalla y se lo contará como un intento más
"""

import random as rn


def es_el_numero(num: int, goal: int) -> bool:
    """
    Compara dos números, retorna si son iguales o no y printea si es mayor o menor.
    Recibe dos enteros.
    Retorna True si los números son iguales, si no, retorna False.
    """
    if num != goal:
        if num < goal:
            print("El número a adivinar es más alto.")
        else:
            print("El número a adivinar es más bajo.")
        return False
    return True


if __name__ == "__main__":
    while True:
        INTENTOS = 5
        NUMERO = rn.randint(1, 500)
        while INTENTOS >= 0:
            if INTENTOS == 0:
                print(f"No has adivinado el número. Era {NUMERO}")
                break
            print(f"Cantidad de intentos restantes: {INTENTOS}")
            try:
                n = int(input("Ingrese un entero: "))
                if es_el_numero(n, NUMERO):
                    print(f"Felicidades, el número era {NUMERO}.")
                    break
            except ValueError:
                print("El valor ingresado no es válido")
            finally:
                INTENTOS -= 1
