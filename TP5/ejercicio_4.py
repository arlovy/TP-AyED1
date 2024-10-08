"""
Todo programa Python es susceptible de ser interrumpido mediante la pulsación de 
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar 
un programa para imprimir los números enteros entre 1 y 100000, y que solicite 
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
"""

def imprimir_numeros() -> None:
    """
        
    """
    n = 1
    while n < 100000:
        try:
            print(n)
        except KeyboardInterrupt:
            confirmation = ""
            while confirmation not in ("s", "n"):
                confirmation = input("Está seguro que quiere terminar el programa (s/n): ").lower()
            if confirmation == "s":
                break
            continue
        finally:
            n += 1

if __name__ == "__main__":
    imprimir_numeros()