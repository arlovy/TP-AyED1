"""
    Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una 
    fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros 
    correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones 
    ni agregados, desarrollar programas que permitan:

    a. Sumar N días a una fecha.
    b. Calcular la cantidad de días existentes entre dos fechas cualesquiera
"""


def fecha_es_valida(dia: int, mes: int, year: int):
    """
    Verifica si los enteros pasados como dia, mes y año corresponden a una fecha válida,
    teniendo en cuenta años bisiestos y los días máximos que puede tener un mes.

    Si la fecha es válida, retorna True. Si la fecha no es válida, retorna False.
    """

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


def diasiguiente(dia: int, mes: int, year: int):
    """
    Esta función recibe tres enteros correspondientes a una fecha.
    Le suma un día a la fecha, y modifica los otros valores si correspondiera.

    Retorna una lista con la fecha modificada.
    """

    if es_bisiesto(year):
        dias_por_mes[2] = 29

    dia += 1
    if dia > dias_por_mes.get(mes):
        mes += 1
        dia = 1
    if mes > 12:
        year += 1
        mes = 1

    if dias_por_mes[2] == 29:
        dias_por_mes[2] = 28

    return [dia, mes, year]


def sumar_tantos_dias(fecha: list[int], dias: int) -> list[int]:
    """
    Esta función toma como parámetro una lista de tres enteros, que representa una fecha,
    y un entero que representa la cantidad de días a sumar.

    Retorna la lista de fecha modificada.
    """

    for _ in range(dias):
        day, month, year = fecha
        fecha = diasiguiente(day, month, year)

    return fecha


def calcular_dias_between(first_date: list[int], second_date: list[int]) -> int:
    """
    Toma dos listas de 3 enteros que representan fechas. Ejecuta la función
    diasiguiente() y cuenta la cantidad de dias hasta que las fechas son iguales.

    Retorna la diferencia de dias entre ambas fechas.
    """
    contador_dias = 0
    while first_date != second_date:
        day, month, year = first_date
        first_date = diasiguiente(day, month, year)
        contador_dias += 1

    return contador_dias


if __name__ == "__main__":

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

    print("1 - Sumar días a una fecha.")
    print("2 - Contar los días entre dos fechas.")

    try:
        option = int(input("Ingrese la opción: "))
        match option:
            case 1:
                day_input = int(input("Ingrese el día: "))
                month_input = int(input("Ingrese el mes: "))
                year_input = int(input("Ingrese el año: "))
                if fecha_es_valida(day_input, month_input, year_input):
                    date_list = [day_input, month_input, year_input]
                    days_to_add = int(input("Ingrese la cantidad de dias a sumar: "))
                    day, month, year = sumar_tantos_dias(date_list, days_to_add)
                    print(f"La fecha resultante es {day}/{month}/{year}")
                else:
                    print("La fecha ingresada no es válida.")


            case 2:
                dates = [[],[]]
                for i in range(2):
                    dates[i].append(int(input("Ingrese el día: ")))
                    dates[i].append(int(input("Ingrese el mes: ")))
                    dates[i].append(int(input("Ingrese el año: ")))
                RESULTADO = calcular_dias_between(dates[0], dates[1])

                print(f"Entre ambas fechas hay {RESULTADO} días de diferencia.")

            case _:
                print("Opcion no valida.")
    except ValueError:
        print("El valor ingresado no es válido.")
