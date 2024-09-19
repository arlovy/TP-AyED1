"""
Los números de claves de dos cajas fuertes están intercalados dentro de un número 
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa 
para obtener ambas claves, donde la primera se construye con los dígitos ubicados 
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en 
posiciones  pares.  Los  dígitos  se  numeran  desde  la  izquierda.  Ejemplo:  Si  clave 
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.
"""

def obtener_claves(clavicula: str):
    """
    Esta función recibe un string y lo divide en dos, uno con los caracteres en
    posiciones pares y otro con caracteres en posiciones impares, y luego
    los retorna en una tupla.
    """
    clavicula1 = ''
    clavicula2 = ''

    for i in range(len(clavicula)):
        if i % 2 == 0:
            clavicula1 += clavicula[i]
        else:
            clavicula2 += clavicula[i]

    return clavicula1, clavicula2

# Ejemplo de uso
clave_maestra = int(input("Ingrese la clave maestra: "))
clave1, clave2 = obtener_claves(clave_maestra)
print("Clave 1:", clave1)
print("Clave 2:", clave2)
