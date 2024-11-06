"""
Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales 
contiene,  identificando  la  cantidad  de  cada  una.  Devolver  un  diccionario  con  los 
resultados.  Luego  desarrollar  un  programa  para  leer  una  frase  e  invocar  a  la 
función  por  cada  palabra  que  contenga  la  misma.  Imprimir  las  palabras  y  la 
cantidad de vocales hallada
"""

def cuenta_vocales(palabra: str) -> dict:
    """
    Recibe un string y cuenta sus vocales.
    Recibe un string.
    Retorna un diccionario {vocal:cantidad}
    """

    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for char in palabra.lower():
        if char in vocales: 
            vocales[char] += 1 
    return vocales


if __name__ == "__main__":
    palabra = "Juniors"
    salida = cuenta_vocales(palabra)
    print("Cantidad de vocales:")
    for voc, cantidad in salida.items():
        print(f"{voc.upper()}: {cantidad}")
