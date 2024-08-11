"""
Una persona desea llevar el control de los gastos realizados al viajar en el subte
rráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un es
quema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarro
llar una función que reciba como parámetro la cantidad de viajes realizados en un 
determinado mes y devuelva el total gastado en viajes. Realizar también un pro
grama para verificar el comportamiento de la función.
"""


def control_de_gastos(boleto: int, viajes_realizados: int):
    """
    Recibe como parámetro un entero correspondiente al precio de un boleto, y
    otro entero correspondiente a una cantidad de viajes realizados.

    Verifica que el número de viajes sea válido. Si no fuera válido, retorna
    -1. Si es válido, retorna el precio total de los viajes del mes, con el
    descuento correspondiente.
    """
    precio_total = boleto * viajes_realizados

    try:
        assert viajes_realizados > 0
    except AssertionError:
        return -1

    if viajes_realizados <= 20:
        return precio_total
    elif 21 <= viajes_realizados <= 30:
        return precio_total * 0.8
    elif 31 <= viajes_realizados <= 40:
        return precio_total * 0.7
    else:
        return precio_total * 0.6


if __name__ == "__main__":
    VALOR_BOLETO = 574
    try:
        viajes = int(input("Ingrese la cantidad de viajes que ha realizado en el mes: "))
        costo_total = control_de_gastos(VALOR_BOLETO, viajes)
        if costo_total != -1:
            print(f"El valor total de los viajes durante el mes es de ${costo_total}")
        else:
            print("El número de viajes ingresado no es válido.")
    except ValueError:
        print("Error. El valor ingresado debe ser un entero.")
