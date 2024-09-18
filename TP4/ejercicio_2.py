"""
Leer  una  cadena  de  caracteres  e  imprimirla  centrada  en  pantalla.  Suponer  que  la 
misma tiene 80 columnas.
"""


def centrar_texto(cadena: str):
    """
    Esta función recibe una cadena y la centra en 80 columnas, printeandola.
    Recibe una cadena.
    No retorna nada.
    """
    columnas = 80
    espacios = (columnas - len(cadena)) // 2
    print("-" + " " * espacios + cadena + " " * espacios + "-")


cadenita = input("Introduce una cadena de caracteres: ")
centrar_texto(cadenita)
