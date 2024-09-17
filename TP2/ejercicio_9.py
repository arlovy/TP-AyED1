"""
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado. 
"""

if __name__ == "__main__":
    num_a = int(input("Ingrese el primer numero: "))
    num_b = int(input("Ingrese el segundo numero: "))
    print(list(filter(lambda x: x % 5 != 0 and x % 7 == 0, list(i for i in range(num_a, num_b + 1)))))