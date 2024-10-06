"""
Desarrollar una función para ingresar a través del teclado un número natural. La 
función rechazará cualquier ingreso inválido de datos utilizando excepciones y 
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese 
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón 
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea 
correcto. Escribir también un programa que permita probar el correcto funciona
miento de la misma
"""

def return_nat() -> int:
    """
    
    """
    try:
        n = int(input("Ingrese un número: "))
        assert n > 0
    except AssertionError:
        print("Error. El número ingresado debe ser mayor a 0.")
        return 0
    except ValueError:
        print("Error. El número ingresado debe ser un entero.")
        return 0
    else:
        return n


if __name__ == "__main__":
    while True:
        out = return_nat()
        if out:
            print(out)
        else:
            print("Ingrese nuevamente.")
