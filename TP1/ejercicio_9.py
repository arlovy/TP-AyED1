"""
    Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso 
    para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y 
    cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón 
    caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso 
    de alguna naranja se encuentra fuera del rango indicado se la clasifica para 
    procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas 
    cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para 
    jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente 
    reparto. Simular el peso de cada unidad generando un número entero al azar entre 
    150 y 350.

    Además, se desea saber cuántos camiones se necesitan para transportar la cose
    cha, considerando que la ocupación del camión no debe ser inferior al 80%; en 
    caso contrario el camión no serán despachado por su alto costo.
"""

import random as rn

rn.seed(1)


def generar_naranjas(n):
    pesos_naranjas = tuple(rn.randint(150, 350) for i in range(n))
    return pesos_naranjas


def clasificar_naranjas(oranges: tuple):
    naranjas_aptas, naranjas_jugo = 0, 0
    promedio_peso = sum(oranges) / len(oranges)

    for orange in oranges:
        if 300 >= orange >= 200:
            naranjas_aptas += 1
        else:
            naranjas_jugo += 1

    return (naranjas_aptas, naranjas_jugo, promedio_peso)


def contar_cajones(good_oranges: int):
    cantidad_cajones = good_oranges // LIMITE_CAJON
    sobrante = good_oranges % LIMITE_CAJON

    return cantidad_cajones, sobrante


def calcular_camiones(cajones, promedio):
    camiones = 0
    cajones_a_despachar = 0
    pass

if __name__ == "__main__":
    LIMITE_CAJON = 100
    LIMITE_PESO = 500
    try:
        naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))
        if naranjas <= 0:
            print("El número ingresado debe ser positivo.")
        else:
            tupla_pesos = generar_naranjas(naranjas)
            aptas, jugo, promedio = clasificar_naranjas(tupla_pesos)
            cajones, sobrante = contar_cajones(aptas)

            if cajones:
                print(f"Se pueden llenar {cajones} cajones.")
            else:
                print("No se puede llenar ningún cajon.")

            if jugo:
                print(f"{jugo} naranjas son para jugo.")
            else:
                print("No hay naranjas para jugo.")

            if sobrante:
                print(f"{sobrante} naranjas sobran para el próximo reparto.")
            else:
                print("No sobra ninguna naranja.")
    except ValueError:
        print("El dato ingresado no es válido.")
