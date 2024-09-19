"""
Se solicita crear un programa para leer direcciones de correo electrónico y verificar 
si representan una dirección válida. Por ejemplo usuario@dominio.com.ar. Para que 
una dirección sea considerada válida el nombre de usuario debe poseer solamente 
caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe 
tener al menos un carácter y tiene que finalizar con .com o .com.ar.  
Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mos-
trar  un  listado  de  todos  los  dominios,  sin  repetirlos  y  ordenados  alfabéticamente, 
recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas.
"""

import re


def es_correo_valido(correo: str):
    """
    Recibe un string y verifica que corresponda a una dirección de correo
    válida.
    Retorna True o False.
    """
    patron = r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|com\.ar)$"
    return re.match(patron, correo) is not None


def obtener_dominio(correo: str):
    """
    Esta función consigue el dominio de un correo electrónico.
    Recibe un string que corresponde a un correo electrónico.
    Retorna su dominio (ej: gmail.com)
    """
    return correo.split("@")[1]


def main():
    """
    Esta función ejecuta el programa.
    """
    dominios = set()  # para no repetir

    while True:
        mail = input(
            "Ingrese una dirección de correo (o presione Enter para finalizar): "
        ).strip()

        if not mail:
            break

        if es_correo_valido(mail):
            dominio = obtener_dominio(mail).lower()
            dominios.add(dominio)
            print(f"'{mail}' es un correo válido.")
        else:
            print(f"'{mail}' no es un correo válido.")

    print()
    print("Lista de dominios únicos, ordenados alfabéticamente:")
    for dominio in sorted(dominios):
        print(dominio)


if __name__ == "__main__":
    main()
