"""
Escribir funciones lambda para:
    a. Informar si un número es oblongo. Se dice que un número es oblongo cuando 
    se puede obtener multiplicando dos números naturales consecutivos. Por ejem
    plo 6 es oblongo porque resulta de multiplicar 2 * 3.

    b. Informar si un número es triangular. Un número se define como triangular si 
    puede expresarse como la suma de un grupo de números naturales consecuti
    vos comenzando desde 1. Por ejemplo 10 es un número triangular porque se 
    obtiene sumando 1+2+3+4.
Ambas funciones lambda reciben como único parámetro el número a evaluar y de
vuelven True o False. No se permite utilizar ayudas externas a las mismas.

"""

es_oblongo = lambda num: any(i * (i + 1) == num for i in range(num)) or num == 0

es_triangular = lambda num: any(
    (i * (i + 1) / 2) == num for i in range(1, num)
)  # formula para numeros triangulares (n+(n+1))/2

if __name__ == "__main__":

    try:
        ingreso = int(input("Ingrese el numero: "))
        if es_oblongo(ingreso):
            print(f"{ingreso} es oblongo.")
        else:
            print(f"{ingreso} no es oblongo.")

        if es_triangular(ingreso):
            print(f"{ingreso} es triangular.")
        else:
            print(f"{ingreso} no es triangular.")
                
    except ValueError:
        print("El dato ingresado debe ser entero.")
