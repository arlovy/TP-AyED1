"""
Escribir una función buscarclave() que reciba como parámetros un diccionario y un 
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el dic-
cionario. Comprobar el comportamiento de la función mediante un programa apro-
piado.
"""

def buscarclave(target: dict, seek: int) -> list:
    return [clave for clave, valor in target.items() if valor == seek]


if __name__ == "__main__":

    goles_jugadores = {
    "Leo Messi": 849,
    "Cristiano Ronaldo": 900,
    "Pelé": 767,
    "Romário": 772,
    "Robert Lewandowski": 600,
    "Zlatan Ibrahimović": 570,
    "Luis Suárez": 530,
    "Karim Benzema": 440,
    "Neymar Jr": 440,
    "Gerd Müller": 735,
    "Eusébio": 620,
    "Ferenc Puskás": 700,
    "Raúl González": 405,
    "Thierry Henry": 405,
    "Aron Lovey": 405,
    "Wayne Rooney": 380
    }

    claves = []

    try:
        valor = int(input("Ingrese el valor: "))
    except ValueError:
        print("Error. El valor ingresado debe ser entero.")
    else:
        claves = buscarclave(goles_jugadores, valor)
    finally:
        if claves:
            print(f"Las claves asociadas al valor {valor} son:")
            for clave in claves:
                print(f"- {clave}")
        else:
            print("No se encontró ninguna clave con el valor ingresado.")