"""
Realizar una función que reciba como parámetros dos cadenas de caracteres con
teniendo números reales, sume ambos valores y devuelva el resultado como un 
número real. Devolver -1 si alguna de las cadenas no contiene un número válido, 
utilizando manejo de excepciones para detectar el error
"""

def concat_sum(n1: str, n2: str) -> int:
    """
    Suma dos strings y los retorna como un dígito entero si no tuviera decimales,
    o float en el caso contrario.
    Recibe dos strings que puedan ser interpretados como números.
    Retorna el resultado de la suma, o -1 si la suma no se pudiera efectuar.
    """
    try:
        firstpar = float(n1)
        secpar = float(n2)
    except ValueError:
        return -1
    else:
        out = firstpar + secpar
        if out.is_integer():
            out = int(out)
        return out

if __name__ == "__main__":
    first = input("Ingrese el primer numero: ")
    second = input("Ingrese el segundo número: ")
    salida = concat_sum(first, second)
    if salida != -1:
        print(salida)
    else:
        print("No se pudo realizar la suma.")
