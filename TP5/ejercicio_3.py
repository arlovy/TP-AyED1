"""
Desarrollar una función que devuelva una cadena de caracteres con el nombre del 
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán 
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función. 
Devolver una cadena vacía si el número de mes es inválido. La detección de meses 
inválidos deberá realizarse a través de excepciones
"""

def return_month(mes:int) -> str:
    """
    Permite conseguir el nombre de un mes en base a su número.
    Recibe un entero que representa el número del mes.
    Retorna un string con el nombre del mes.
    """
    meses = ("Enero",
             "Febrero",
             "Marzo",
             "Abril",
             "Mayo",
             "Junio",
             "Julio",
             "Agosto",
             "Septiembre",
             "Octubre",
             "Noviembre",
             "Diciembre")

    try:
        return meses[mes - 1]
    except IndexError:
        return ""


if __name__ == "__main__":
    try:
        n = int(input("Ingrese el mes: "))
        salida = return_month(n)
        if salida:
            print(salida)
        else:
            print("El mes ingresado no existe.")
    except ValueError:
        print("El mes ingresado debe ser un entero.")
