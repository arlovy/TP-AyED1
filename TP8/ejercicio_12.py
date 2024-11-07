"""
Una  librería  almacena  su  lista  de  precios  en  un  diccionario.  Diseñar  un  programa 
para  crearlo,  incrementar  los  precios  de  los  cuadernos  en  un  15%,  imprimir  un 
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más 
costoso que venden en el comercio.
"""

def stock(precios: dict, item: str, price: float) -> dict:
    """
    Carga un item y su precio en un diccionario y lo retorna.
    Recibe un diccionario donde cargar los datos, un item que será la clave y un float.
    Retorna el diccionario con la nueva clave-valor.
    """
    precios[item] = price
    return precios


def incrementar_cuadernos(precios:dict) -> dict:
    """
    Revisa el diccionario y incrementa en un 15% los precios de 
    todos los items con el nombre "cuaderno".
    Recibe el diccionario con productos.
    Retorna el diccionario con los precios modificados.
    """
    for item in precios:
        if 'cuaderno' in item.lower():
            precios[item] *= 1.15
    return precios


def mascaro(precios: dict) -> tuple:
    """
    Retorna el elemento con el precio más alto del diccionario de
    productos.
    Recibe un diccionario.
    Retorna una tupla.
    """
    if precios:
        maximo = max(precios, key=precios.get)
        return maximo, precios[maximo]
    return None, None

if __name__ == "__main__":
    precios_libreria = {}

    while True:
        producto = input("\n Ingrese el nombre del producto (S para salir): ")
        if producto.upper() == 'S':
            break

        if producto not in precios_libreria:
            try:
                precio = float(input("Precio del producto: "))
                stock(precios_libreria, producto, precio)
            except ValueError:
                print("Ingrese un precio válido.")
        else:
            print("El producto ingresado ya existe.")

    incrementar_cuadernos(precios_libreria)
    print("Stock actual:")
    for producto, precio in precios_libreria.items():
        if 'cuaderno' in producto:
            print(f"- {producto}: ${precio:.2f} (+15%)")
        else:
            print(f"- {producto}: ${precio:.2f}")

    producto, precio = mascaro(precios_libreria)
    print(f"\nProducto más caro: '{producto}' - ${precio}")
