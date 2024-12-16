"""
Desarrollar una función que reciba un número binario y lo devuelva convertido a
base decimal.
"""

def binario_a_decimal(n:int, potencia:int = 0) -> int:
    """
    Convierte un número binario a decimal.
    Recibe un número binario expresado en entero, y una potencia que
    va variando segun la posición del digito.
    """
    if any(digit not in ["1", "0"] for digit in str(n)):
        raise ValueError("El numero no es binario.")
    if n == 0:
        return 0
    return (n % 10) * (2 ** potencia) + binario_a_decimal(n // 10, potencia + 1)