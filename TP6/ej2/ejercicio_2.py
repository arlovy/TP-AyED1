"""
Escribir un programa que permita dividir un archivo de  texto cualquiera  en partes 
que  se  puedan  enviar  por  correo  electrónico.  El  tamaño  máximo  de  las  partes  se 
ingresa  por  teclado.  Los  nombres  de  los  archivos  generados  deben  respetar  el 
nombre  original  con  el  agregado  de  un  sufijo  que  indique  de  qué  parte  se  trata. 
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuar-
se después del delimitador del mismo. Mostrar un mensaje de error si el proceso no 
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en 
memoria.
"""

from math import ceil

def dividir_archivo(n:int, ruta:str) -> None:
    """
    Divide un archivo de texto en partes con una longitud N.
    Recibe un entero que representa la cantidad de partes, y un string con la ruta del archivo.
    No retorna nada.
    """

    try:
        with open(rf"TP6\ej2\{ruta}", 'r', encoding='utf-8') as myfile:
            contenido = myfile.read()
            longitud = len(contenido)
            parte = 0

            try:
                if n > longitud:
                    raise ValueError("La cantidad de caracteres especificada es mayor al texto.")

                cantidad = longitud / n
                if not longitud % n:
                    cantidad = cantidad // longitud + 1
                cantidad = int(cantidad)

                for _ in range(cantidad):
                    fragmento = contenido[:n]
                    contenido = contenido[n:]
                    parte += 1

                    archivo = f"parte{parte}.txt"
                    with open(archivo, 'w', encoding='utf-8') as partes_correo:
                        partes_correo.write(fragmento)
            except ValueError as e:
                print(e)

    except FileNotFoundError:
        print("El archivo especificado no se ha encontrado.")

if __name__ == "__main__":
    size = int(input("Ingrese el tamaño de cada parte: "))
    RUTA_FILE = input("Ingrese el nombre del archivo: ")
    dividir_archivo(size, RUTA_FILE)
