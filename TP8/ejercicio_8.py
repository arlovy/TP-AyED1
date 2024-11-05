"""
Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
"""

if __name__ == "__main__":
    dic_cuadrados = {num:num**2 for num in range(1,21)}

    print(dic_cuadrados)