"""
La función de Ackermann A(m,n) se define de la siguiente forma:
n+1 si m = 0
A(m-1,1) si n = 0
A(m-1,A(m,n-1)) de otro modo
Imprimir un cuadro con los valores que adopta la función para valores de m entre 0 
y 3 y de n entre 0 y 7.
"""

def ackerman(m: int, n: int) -> int:
    """
    Calcula valores de la función de Ackerman.
    Recibe dos valores enteros positivos de m y n.
    Retorna el valor de m,n dentro de la función de Ackerman.
    """
    if m < 0 or n < 0:
        raise ValueError("Los enteros deben ser positivos.")
    if m == 0:
        return n + 1
    if n == 0:
        return ackerman(m - 1, 1)
    return ackerman(m - 1, ackerman(m, n - 1))

#lo sigo despues
