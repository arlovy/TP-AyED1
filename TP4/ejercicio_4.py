"""
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y 
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En 
qué cambiaría la función si el rango de valores fuese diferente?
"""


def entero_a_romano(num: int):
    """
    Esta función convierte un número entero en un número romano.
    Recibe un entero.
    Retorna un string.
    """
    if not 0 < num <= 3999:
        return "Número fuera de rango"

    valores_romanos = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    resultado = ""

    for valor, simbolo in valores_romanos:
        while numero >= valor:
            resultado += simbolo
            num -= valor

    return resultado


numero = int(input("Ingrese el número: "))
romano = entero_a_romano(numero)
print(f"El número {numero} en números romanos es: {romano}")
