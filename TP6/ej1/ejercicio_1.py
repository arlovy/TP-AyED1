"""
Escribir un programa que lea un archivo de texto conteniendo un conjunto de ape
llidos y nombres en formato "Apellido, Nombre" y guarde en el archivo 
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cade
na "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los 
terminados en "EZ". Descartar el resto. Ejemplo:
    Arslanian, Gustavo –> ARMENIA.TXT
    Rossini, Giuseppe –> ITALIA.TXT
    Pérez, Juan
    Smith, John –> ESPAÑA.TXT –> descartar
 El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor.
"""

try:
    with open("nombres.txt","rt", encoding="utf-8-sig") as nombres_archivo:
        nombres = nombres_archivo.readlines() # lee cada linea
        # saca el salto de linea y splitea
        nombres = list(map(lambda x: x.strip().split(","), nombres))

        for nombre in nombres:
            if nombre[1].lower()[-2:] == "ez":
                with open("ESPAÑA.txt", "at", encoding="utf-8-sig") as armenia:
                    armenia.write(",".join(nombre) + "\n")

            match nombre[1].lower()[-3:]:
                case "ian":
                    with open("ARMENIA.txt", "at", encoding="utf-8-sig") as armenia:
                        armenia.write(", ".join(nombre) + "\n")
                case "ini":
                    with open("ITALIA.txt", "at", encoding="utf-8-sig") as armenia:
                        armenia.write(",".join(nombre) + "\n")
except FileNotFoundError:
    print("Error: No se puede encontrar el archivo 'nombres.txt'")
