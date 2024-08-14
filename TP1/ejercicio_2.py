"""
Desarrollar una función que reciba tres números enteros positivos correspondientes 
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe 
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos. 
Devolver True o False según la fecha sea correcta o no. Realizar también un 
programa para verificar el comportamiento de la función.
"""


def fecha_es_valida(dia: int, mes: int, year: int):
    """
    Verifica si los enteros pasados como dia, mes y año corresponden a una fecha válida,
    teniendo en cuenta años bisiestos y los días máximos que puede tener un mes.

    Si la fecha es válida, retorna True. Si la fecha no es válida, retorna False.
    """

    dias_por_mes = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    if dia == 29 and mes == 2 and es_bisiesto(year):
        return True
    if dia > dias_por_mes.get(mes) or dia < 1:
        return False
    else:
        return True


def es_bisiesto(year: int):
    """
    Verifica que el año sea bisiesto.

    Si es divisible por 4, o también es divisible por 400 pero no por 100, retorna True.
    Si no se cumple esta condición, retorna False.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":
    try:
        day = int(input("Ingrese el dia: "))
        month = int(input("Ingrese el mes: "))
        year_input = int(input("Ingrese el año: "))
        print(fecha_es_valida(day, month, year_input))
    except ValueError:
        print("Error. El valor ingresado no es un entero")
