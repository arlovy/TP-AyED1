"""
Definir  un  conjunto  con  números  enteros  entre  0  y  9.  Luego  solicitar  valores  al 
usuario y  eliminarlos  del conjunto mediante  el método  remove,  mostrando  el con-
tenido  del  conjunto  luego  de  cada  eliminación.  Finalizar  el  proceso  al  ingresar  -1. 
Utilizar  manejo  de  excepciones  para  evitar  errores  al  intentar  quitar  elementos 
inexistentes.
"""

def eliminar_numero(conjunto: set, num: int):
    '''
    Elimina un número determinado de un conjunto.
    Recibe un conjunto de numeros enteros, y un entero a eliminar.
    Retorna el conjunto sin el entero especificado.
    '''
    return conjunto.remove(num)


if __name__ == "__main__":

    myset = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    while True:
        try:
            num_a_eliminar = int(input("Ingrese el numero a eliminar (-1 para salir): "))
            if num_a_eliminar == -1:
                print("Saliendo...")
                break
            print(eliminar_numero(myset, num_a_eliminar))

        except KeyError:
            print("El número a eliminar no existe en el conjunto.")
        except ValueError:
            print("Ingrese un número válido.")
