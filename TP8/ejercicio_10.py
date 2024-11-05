"""
Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario 
y  una  lista  de  claves.  La  función  debe  eliminar  del  diccionario  todas  las  claves 
contenidas  en  la  lista,  devolviendo  el  diccionario  modificado  y  un  número  entero 
que represente la cantidad de claves eliminadas. Desarrollar también un programa 
para verificar su comportamiento.
"""

def eliminarclaves(dict_: dict, claves: list[str]) -> tuple:
    """
    Elimina claves y sus valores de un diccionario cualquiera.
    Recibe un diccionario y una lista de strings que indican las claves.
    Retorna una tupla (diccionario nuevo, cantidad de elementos eliminados).
    """
    eliminados = 0
    for key in claves:
        if key in dict_:
            try:
                dict_.pop(key)
            except Exception:
                return dict_, 0
            eliminados += 1
    return dict_, eliminados


if __name__ == "__main__":
    diccionario = {
    "Nombre" : "Pedro",
    "Apellido" : "Perez"
    }
    print(eliminarclaves(diccionario, ["Nombre"]))