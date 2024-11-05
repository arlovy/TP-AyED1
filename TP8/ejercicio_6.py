"""
Ingresar una  frase desde  el teclado y  usar  un conjunto  para  eliminar  las palabras 
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras 
ordenadas  según  su  longitud.  Los  signos  de  puntuación  no  deben  afectar  el 
proceso
"""

if __name__ == "__main__":
    frase = input("Ingrese su frase: ")
    unicas = set(map(lambda x: x.replace(",","").replace(".","").capitalize(), frase.lower().split(" ")))
    for num, elem in enumerate(sorted(unicas, key=lambda x: len(x)), start=1):
        print(f"{num}.{elem}")