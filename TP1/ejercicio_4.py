"""
Un comercio de electrodomésticos necesita para su línea de cajas un programa que 
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan 
dos números enteros, correspondientes al total de la compra y al dinero recibido. 
Informar cuántos billetes de cada denominación deben ser entregados como vuelto, 
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes 
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el 
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta 
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se 
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 
billete de $200, 1 billete de $100 y 3 billetes de $10
"""


def calcular_cambio(precio: int, pago: int, billetes: list):
    """
    Esta función toma como parámetro dos enteros que representan un precio y
    la cifra pagada por el cliente, además de una lista con las denominaciones
    de los billetes ordenadas de mayor a menor.

    Consulta los billetes vigentes y retorna una lista con la cantidad de 
    billetes de cada denominación necesarios para dar el vuelto con la 
    menor cantidad de billetes posibles.

    Si el pago no fuese suficiente para pagar por la compra, retorna la lista
    de vueltos con -1 como único valor. Si el pago es justo, retorna la lista
    con -2 como único valor.
    """

    vuelto = []
    pago_a_procesar = pago - precio
    restante = 0

    if pago_a_procesar < 0 :
        vuelto.append(-1)
    elif pago_a_procesar == 0:
        vuelto.append(-2)
    else:
        for billete in billetes:
            if pago_a_procesar % billete == pago_a_procesar:
                vuelto.append(0)
            else:
                vuelto.append(pago_a_procesar // billete)
                pago_a_procesar %= billete
    
    if pago_a_procesar > 0:
        restante += pago_a_procesar
    return vuelto, restante


def verificar_entradas(precio: int, pago: int):
    """
    Función booleana que retorna True solo si sus dos parámetros son
    positivos.
    """
    if precio < 0 or pago < 0:
        return False
    return True


if __name__ == "__main__":
    try:
        billetes = (5000, 1000, 500, 200, 100, 50, 10)
        precio_compra = int(input("Ingrese el precio total de la compra: "))
        total_recibido = int(input("Ingrese el valor recibido: "))

        if verificar_entradas(precio_compra, total_recibido):

            vuelto, restante = calcular_cambio(precio_compra, total_recibido, billetes)

            if any(vuelto):

                match vuelto[0]:
                    case -1:
                        print("El monto abonado no es suficiente para pagar la compra.")
                    case -2:
                        print("No es necesario dar vuelto.")
                    case _:

                        print("VUELTO TOTAL:")
                        for i in range(len(vuelto)):
                            if vuelto[i] != 0:
                                print(f"Billetes de ${billetes[i]}: {vuelto[i]}")

                        if restante > 0:
                            print("MONTO RESTANTE POR FALTA DE BILLETES VALIDOS:")
                            print(f"${restante}")

            else:
                print("No hay billetes con la denominación suficiente para dar el vuelto.")

        else:
            print("Todos los valores deben ser positivos.")

    except ValueError:
        print("Todos los valores ingresados deben ser enteros.")
