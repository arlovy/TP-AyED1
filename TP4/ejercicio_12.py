"""
Escribir un programa para crear una lista por comprensión con los naipes de la ba-
raja española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2 
Oros"... ]. Imprimir la lista por pantalla.
"""

palos = ('Oros', 'Bastos', 'Espadas', 'Copas')
barajas = [' '.join([str(x), y]) for y in palos for x in range(1, 13)]
print(barajas)