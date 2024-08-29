"""
    Desarrollar una función que reciba como parámetros dos números enteros positivos 
    y devuelva como valor de retorno el número que resulte de concatenar ambos 
    parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se per
    mite utilizar facilidades de Python no vistas en clase.
"""


def concatenar_numeros(num1: int, num2: int) -> str:
    """
    Esta función toma como parámetros dos numeros enteros positivos.

    Retorna un string con la concatenación de ambos números.
    """
    assert num1 > 0 and num2 > 0
    return f"{num1}{num2}"

if __name__ == "__main__":
    try:
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        print(concatenar_numeros(n1, n2))
    except ValueError:
        print("Los valores ingresados no son válidos.")
    except AssertionError:
        print("Los valores deben ser positivos.")
