"""
Se dispone de tres formatos diferentes de archivos de texto en los que se almace-
nan datos de empleados, detallados más abajo. Desarrollar un programa para cada
uno de los formatos suministrados, que permitan leer cada uno de los archivos y
grabar los datos obtenidos en otro archivo de texto con formato CSV.
"""


def formatear_1(ruta: str, salida: str) -> None:
    """
    Lee un archivo A formateado con espacios y lo escribe en un archivo B.
    Recibe dos rutas en foramto string, la primera para el archivo A y la segunda
    para el archivo B.
    No retorna nada.
    """
    try:
        with open(ruta, "rt", encoding="utf-8") as archivo, open(
            salida, "wt", encoding="utf-8"
        ) as archivofinal:
            lineas = archivo.readlines()
            for linea in lineas:
                nombre = linea[:17].strip()
                dni = linea[17:28].strip()
                direccion = linea[28:].strip()
                archivofinal.write(f"{nombre},{dni},{direccion}\n")
    except FileNotFoundError:
        print("No se encontro el archivo 1.")


def formatear_2(ruta: str, salida: str) -> str:
    """
    Lee un archivo A formateado de manera específica y lo escribe en un archivo CSV B.
    Recibe dos rutas en formato string, la primera para el archivo A y la segunda para el
    archivo B.
    No retorna nada.
    """
    try:
        with open(ruta, "rt", encoding="utf-8") as archivo, open(
            salida, "wt", encoding="utf-8"
        ) as archivofinal:
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip()
                inicio = 0
                data = []
                largo = int(linea[inicio : inicio + 2])
                for i in range(3):
                    campo = linea[inicio + 2 : inicio + largo + 2]
                    inicio += largo + 2
                    data.append(campo)
                    if i == 2:
                        break
                    largo = int(linea[inicio : inicio + 2])
                archivofinal.write(f'{",".join(data)}\n')
    except FileNotFoundError:
        print("No se encontro el archivo.")


if __name__ == "__main__":
    formatear_1("archivo1.txt", "output_1.txt")
    formatear_2("archivo2.txt", "output_2.txt")
