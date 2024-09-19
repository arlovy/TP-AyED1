"""
Un hotel necesita un programa para gestionar la operación de sus habitaciones. El 
hotel  cuenta  con  10  pisos  y  6  habitaciones  por  piso.  Por  cada  huésped  o  grupo 
familiar que se aloja en el mismo se registra la siguiente información:

    ∑ DNI del cliente (número entero)
    ∑ Apellido y Nombre
    ∑ Fecha de ingreso (DDMMAAAA)
    ∑ Fecha de egreso (DDMMAAAA)
    ∑ Cantidad de ocupantes

Se solicita desarrollar un programa que utilice arreglos para realizar las siguientes 
tareas:

    a. Registrar el ingreso de huéspedes al hotel, hasta que se ingrese un número de 
    DNI igual a -1. Tener en cuenta que los números de DNI no pueden repetirse y 
    que la fecha de salida debe ser mayor a la de entrada. El piso y habitación son 
    asignados arbitrariamente, y no puede asignarse una habitación ya otorgada. 
    b. Finalizado el ingreso de huéspedes se solicita:
        1. Mostrar el piso con mayor cantidad de habitaciones ocupadas.
        2. Mostrar cuántas habitaciones vacías hay en todo el hotel.
        3. Mostrar el piso con mayor cantidad de personas.
        4. Mostrar cuál será la próxima habitación en desocuparse. La fecha actual se 
        ingresa por teclado. Mostrar todas las que correspondan.
        5. Mostrar un listado de todos los huéspedes registrados en el hotel, ordenado 
        por apellido.
"""