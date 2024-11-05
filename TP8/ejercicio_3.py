"""
Desarrollar  un  programa  que  utilice  una  función  que  reciba  como  parámetro  una 
cadena  de  caracteres  conteniendo  una  dirección  de  correo  electrónico  y  devuelva 
una tupla con las distintas partes que componen dicha dirección. Ejemplo: 
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar 
formatos de fecha inválidos y devolver una tupla vacía.
"""
import re

def partir_correo(direccion:str) -> tuple[str]:
    """
    Parte una dirección de correo electrónico en usuario, dominio y extensiones.
    Recibe un string que representa una dirección de email.
    Retorna una tupla de sub-strings.
    """
    patron = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"

    if not re.match(patron, direccion):
        return tuple()

    usuario, dominio = direccion.split("@")
    dominio = dominio.split(".")

    return usuario, *dominio


if __name__ == "__main__":
    mail = input("Ingrese la dirección de correo electrónico que desea partir: ")
    salida = partir_correo(mail)
    if salida:
        print(salida)
    else:
        print("El correo no es válido.")