"""
Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los 
elementos de la primera que sean impares. El proceso deberá realizarse utilizando 
la función filter(). Imprimir las dos listas por pantalla.
"""

import random as rn

lista_salazar = [rn.randint(1,100) for i in range(rn.randint(1,100))]

lista_impares = list(filter(lambda x: x % 2 != 0, lista_salazar))

print(lista_salazar)
print()
print(lista_impares)