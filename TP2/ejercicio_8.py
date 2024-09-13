"""
Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200.
"""

lista_impares = list(filter(lambda x: x % 2 != 0, list(i for i in range(100,201))))

print(lista_impares)