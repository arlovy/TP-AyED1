"""
Escribir  una  función  que  indique  si  dos  fichas  de  dominó  encajan  o  no.  Las  fichas 
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True 
o False. Escribir también un programa para verificar su comportamiento. Considerar 
el uso de conjuntos para resolver este ejercicio.
"""
def unir_fichas(ficha1:tuple, ficha2:tuple) -> bool:
    '''
    Compara dos tuplas de enteros y retorna si algun valor coincide entre ellas.
    Recibe dos tuplas con enteros.
    Retorna un booleano.
    '''
    return not set(ficha1).isdisjoint(set(ficha2))

if __name__ == "__main__":
    cosa1 = (3, 4)
    cosa2 = (5, 4)

    if unir_fichas(cosa1, cosa2):
        print(f"Las fichas {cosa1} y {cosa2} encajan.")
    else:
        print(f"Las fichas {cosa1} y {cosa2} no encajan.")
