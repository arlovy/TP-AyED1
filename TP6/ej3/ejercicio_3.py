"""
Una  institución  deportiva  necesita  clasificar  a  sus  atletas  para  inscribirlos  en  los 
próximos  Juegos  Panamericanos.  Para  eso  encargó  la  realización  de  un  programa 
que incluya las siguientes funciones:

GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas 
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una 
línea distinta. Ejemplo:
<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>
< . . . >

GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atle-
tas,  leyendo  los  datos  del archivo  generado  en  el paso  anterior.  La  disciplina  y  el 
promedio deben grabarse en líneas diferentes. Ejemplo:
<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>

MostrarMasAltos()  Muestra  por  pantalla  las  disciplinas  deportivas  cuyos  atletas 
superan la estatura promedio general. Obtener los datos del segundo archivo.
"""

def grabarrangoalturas() -> None:
    """
    Genera un archivo 'altura.txt' y permite al usuario ingresar alturas de deportistas
    para distintos deportes.
    No retorna y no recibe nada.
    """
    with open(r'TP6\ej3\altura.txt', 'w', encoding='utf-8') as alturas:
        while True:
            deporte = input("Ingrese el deporte ('S' para salir): ")
            if deporte.upper() == 'S':
                break
            alturas.write(deporte + '\n')
            num = 0
            while True:
                num += 1
                altura = input(f"Ingrese la altura del {num}° atleta ('S' para salir): ")
                if altura.upper() == 'S':
                    break
                alturas.write(altura + '\n')
            alturas.write('\n')


def grabarpromedio() -> None:
    """
    Lee el archivo 'altura.txt' y genera un archivo con los promedios de altura por deporte.
    No recibe ni retorna nada.
    """
    with open(r'TP6\ej3\altura.txt', 'r', encoding='utf-8') as alturas:
        contenido = alturas.readlines()

        with open(r'TP6\ej3\promedios.txt', 'w', encoding='utf-8') as promedios:
            registro_alturas = []

            for linea in contenido:
                linea = linea.strip()
                try:
                    altura = float(linea)
                    registro_alturas.append(altura)
                except ValueError:
                    if registro_alturas:
                        promedio = sum(registro_alturas) / len(registro_alturas)
                        promedios.write(f"{promedio}")
                        registro_alturas = []
                    promedios.write(linea + '\n')


def mostrarmasaltos() -> None:
    """
    Lee el archivo 'promedios.txt' y muestra el deporte cuya altura promedio supera
    al promedio general.
    No recibe ni retorna nada.
    """
    with open(r'TP6\ej3\promedios.txt', 'r', encoding='utf-8') as archivo:
        contenido = archivo.readlines()
        promedios = []
        deportes = []

        for linea in contenido:
            linea = linea.strip()
            try:
                promedio = float(linea)
                promedios.append(promedio)
            except ValueError:
                if linea:
                    deportes.append(linea)

        if promedios:
            max_promedio = sum(promedios) / len(promedios)
            print(f"Promedio de alturas: {max_promedio:.2f}")
            print("Deportes cuyos atletas superan la altura promedio:")

            for i, _ in enumerate(promedios):
                if promedios[i] > max_promedio:
                    print(deportes[i])
        else:
            print("Los promedios del archivo no son válidos.")


if __name__ == "__main__":
    grabarrangoalturas()
    grabarpromedio()
    mostrarmasaltos()
