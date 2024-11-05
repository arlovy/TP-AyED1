"""
En geometría un vector es un segmento de recta orientado que va desde un punto 
A hasta un punto B. Los vectores en el plano se representan mediante un par orde-
nado  de  números  reales  (x,  y)  llamados  componentes.  Para  representarlos  basta 
con unir el origen de coordenadas con el punto indicado en sus componentes: 
Dos  vectores  son  ortogonales  cuando  son  perpendiculares  entre  sí.  Para  determi-
narlo basta calcular su producto escalar y verificar si es igual a 0. Ejemplo: 

A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales

Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor 
de verdad indicando si son ortogonales o no. Desarrollar también un programa que 
permita verificar el comportamiento de la función.
"""

def is_ortogonal(vector1:tuple, vector2:tuple) -> int:
    """
    Recibe dos tuplas que representan los vértices de vectores y verifica
    si son ortogonales.
    Recibe dos tuplas con enteros, de la misma longitud.
    Retorna un valor booleano.
    """
    return not bool(sum(a * b for a, b in zip(vector1, vector2)))


if __name__ == "__main__":

    cosa1 = (3, 4)
    cosa2 = (-4, 3)

    if is_ortogonal(cosa1, cosa2):
        print(f"Los vectores {cosa1} y {cosa2} son ortogonales.")
    else:
        print(f"Los vectores {cosa1} y {cosa2} no son ortogonales.")
