"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho-
rarios, y luego escribir un programa que las vincule:
a. Ingresar  una  fecha  desde  el  teclado,  verificando  que  corresponda  a  una  fecha 
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular  la  diferencia  entre  dos  horarios.  Si  el  primer  horario  fuera  mayor  al 
segundo  se  considerará  que  el  primero  corresponde  al  día  anterior.  En  ningún 
caso la diferencia en horas puede superar las 24 horas.
"""

def ingresar_fecha() -> tuple:
    """
    Solicita una fecha al usuario y la retorna en formato de tuplas.
    No recibe nada.
    Retorna una tupla (año,mes,dia).
    """
    while True:
        try:
            year = int(input("Ingrese un año: "))

            mes = int(input("Ingrese un mes: "))
            if not mes in dates.keys():
                print("Error, mes no válido. Ingrese la fecha nuevamente.")
                continue

            dia = int(input("Ingrese el día: "))
            if dia < 1 or dia > dates[mes]:
                print("Error, el día ingresado no es válido. Ingrese la fecha nuevamente.")
                continue

            fecha = (year,mes,dia)
        except Exception as e:
            print("Ha ocurrido un error en el ingreso de los datos.")
            print(f"Error: {e}\n")
            continue
        else:
            print("La fecha es válida.")
            return fecha


def sumar_dias(fecha: tuple[int], n_dias: int) -> tuple:
    """
    Permite sumar N cantidad de días a una fecha y la retorna como tupla.
    Recibe una tupla de enteros (año,mes,dia) y N dias a sumar.
    Retorna la tupla actualizada.
    """
    new_day = fecha[2] + n_dias
    new_month = fecha[1]
    new_year = fecha[1]
    if new_day > dates[fecha[1]]:
        new_month += 1
        new_day -= dates[fecha[1]]

    if new_month > 12:
        new_month = 1
        new_year += 1

    return (new_year, new_month, new_day)


def ingresar_horario() -> int:
    """
    Solicita al usuario un horario y lo retorna si es válido.
    No recibe ningún parámetro.
    Retorna un entero tal que HoraMinutos
    """
    while True:
        try:
            hora = int(input("Ingrese la hora: "))
            if hora > 23 or hora < 00:
                print("Hora no válida. Ingrese nuevamente.")
                continue

            minutos = int(input("Ingrese los minutos: "))
            if minutos < 0 or minutos > 60:
                print("Minutos no válidos. Ingrese la hora nuevamente.")
                continue

            horario = (hora * 100) + minutos

        except Exception as e:
            print("Ha ocurrido un error en la carga de la hora. Intente nuevamente.")
            print(f"Error {e}")
            continue
        else:
            print("Hora válida.")
            return horario


def diferencia_horarios(hora1:int, hora2:int) -> int:
    """
    Recibe dos horarios tal que HoraMinutos (ej, 2359) y retorna la diferencia entre ellos.
    Recibe dos enteros.
    Retorna un entero con la diferencia horaria en el formato horasminutos.
    """
    if hora1 > hora2:
        return hora1 - hora2
    elif hora1 < hora2:
        return hora2 - hora1
    else:
        return 2400


if __name__ == "__main__":
    dates = {
        1: 31, 2: 28, 3: 31,
        4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30,
        10: 31, 11: 30, 12: 31
    }

    opciones = [
        "Verificar fecha",
        "Sumar dias a una fecha",
        "Verificar horario",
        "Ver diferencia entre dos horarios"
    ]

    for num, opcion in enumerate(opciones):
        print(f"{num + 1}.{opcion}")
    
    user_input = int(input("Ingrese la opción: "))
    match user_input:
        case 1:
            ingresar_fecha()
        case 2:
            fecha = ingresar_fecha()
            try:
                dias = int(input("Ingrese los días a sumar: "))
            except ValueError:
                print("Error, el numero ingresado no es entero.")
            print(sumar_dias(fecha, dias))
        case 3:
            ingresar_horario()
        case 4:
            hour1 = ingresar_horario()
            hour2 = ingresar_horario()
            salida = diferencia_horarios(hour1, hour2)
            print(f"La diferencia es de {salida // 100} horas y {salida % 100} minutos.")
        case _:
            print("Opción no válida.")