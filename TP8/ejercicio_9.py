"""
Escribir  un  programa  que  permita  ingresar  un  número  entero  N  y  genere  un 
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la 
tabla de multiplicar con el formato apropiado.
"""

if __name__ == "__main__":
    n = int(input("Ingrese un entero: "))
    diccionario = {i: n * i for i in range(1, 13)}
    for multiplo, resultado in diccionario.items():
        print(f"{n} x {multiplo} = {resultado}")
