"""
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento.
"""

def string_capicuo(string: str):
    for i in range(len(string) // 2):
        if string[i].lower() != string[len(string) - 1 - i].lower():
            return False
    return True


if __name__ == "__main__":
    cadena = input("Ingrese la cadena: ")
    if cadena.isalpha():
        if string_capicuo(cadena):
            print(f"{cadena} es capicúa.")
        else:
            print(f"{cadena} no es capicúa.")
    else:
        print("La cadena ingresada no es válida.")