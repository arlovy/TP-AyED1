"""
Escribir  una  función  que  reciba  como  parámetro  una  tupla  conteniendo  una  fecha 
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada 
en formato extendido. La función debe contemplarse que el año se ingrese en dos 
dígitos,  los  que  serán  interpretados  según  un  año  de  corte  definido  dentro  del 
programa.  Cualquier  año  mayor  que  éste  se  considerará  del  siglo  pasado.  Por 
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030" 
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de 
1931".  Si  el  año  se  ingresa  en  cuatro  dígitos  el  año  de  corte  no  será  tenido  en 
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y 
mostrar el resultado.
"""

def fecha_to_text(date: tuple[int, int, int]) -> str:
    """
    Convierte una tupla de enteros (dia,mes,año {ultimos dos digitos}) en una cadena de texto.
    Recibe una tupla con tres enteros (dia,mes,año).
    Retorna una cadena.
    """

    day, month, year = date
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    cut = 30
    if year > cut:
        year += 1900
    else:
        year += 2000
    return f"{day} de {months[month - 1]} de {year}"


if __name__ == "__main__":
    try:
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        gregoriano = int(input("Ingrese el año: ")) #me niego rotundamente a escribir anio

        if len(str(gregoriano)) > 2:
            print("El año debe tener únicamente dos dígitos.")
        else:
            fecha = (dia, mes, gregoriano)
            print(fecha_to_text(fecha))
    except ValueError:
        print("Error. Los valores ingresados deben ser numéricos.")
