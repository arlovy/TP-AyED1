"""
    La siguiente función permite averiguar el día de la semana para una fecha determi
    nada. La fecha se suministra en forma de tres parámetros enteros y la función de
    vuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para 
    imprimir por pantalla el calendario de un mes completo, correspondiente a un mes 
    y año cualquiera basándose en la función suministrada. Considerar que la semana 
    comienza en domingo.
"""

def diadelasemana(dia,mes,anio):
    """
    Esta funcion hace cosas
    """
    if mes < 3:
        mes = mes + 10 
        anio = anio - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem


def es_bisiesto(year: int) -> bool:
    """
    Verifica que el año sea bisiesto.

    Si es divisible por 4, o también es divisible por 400 pero no por 100, retorna True.
    Si no se cumple esta condición, retorna False.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def mostrar_calendario(mes: int,anio: int) -> None:
    """
    Esta función toma como parámetros dos enteros correspondientes a un mes y un año.

    Para cada fecha del mes indicado, imprime qué día es.

    No retorna nada.
    """
    dias_por_mes = (31, 29 if es_bisiesto(anio) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    nombre_dias = ("Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado")
    primer_dia_mes = diadelasemana(1,mes,anio)

    if mes > 12 or mes < 1:
        print("El mes ingresado no es válido.")
    else:
        for i in range(1, dias_por_mes[mes - 1] + 1):
            primer_dia_mes = diadelasemana(i, mes, anio)
            print(f"{nombre_dias[primer_dia_mes]} {i}")


if __name__ == "__main__":
    try:
        month = int(input("Introduzca el mes: "))
        year = int(input("Introduzca el año: "))
        mostrar_calendario(month,year)
    except ValueError:
        print("Debe ingresar enteros.")
