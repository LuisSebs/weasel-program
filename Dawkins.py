import random
import string

def calificacion(cadena):

    """
        Regresa la calificacion de la cadena
    """

    calificacion_maxima = len(objetivo)
    calificacion_cadena = calificacion_maxima
    for i in range(len(cadena)):
        if (cadena[i] != objetivo[i]):
            calificacion_cadena-=1
    return calificacion_cadena

objetivo = "METHINKS IT IS LIKE A WEASEL"
caracteres = string.ascii_uppercase + " "
probabilidad = 0.05
calificaciones = list()
poblacion = list()
optimo = list()

# Generamos caracteres aleatorios
for _ in range(len(objetivo)):
    optimo.append(random.choice(caracteres))

# Mientras no encontremos al optimo
while calificacion(optimo) != len(objetivo):

    # Hacemos 100 copias
    for _ in range(100):
        poblacion.append(optimo.copy())

    # Mutamos
    for copia in poblacion:
        for i in range(len(copia)):
            if random.random() < probabilidad:
                copia[i] = random.choice(caracteres)

    # Asignamos calificaciones
    calificaciones = [ calificacion(x) for x in poblacion ]

    # Obtenemos al optimo
    mas_alto = 0;
    for i in range(len(calificaciones)):
        calificacion_cadena = calificaciones[i]
        if calificacion_cadena >= mas_alto:
            optimo = poblacion[i]
            mas_alto = calificacion_cadena

    # Mostramos la evolucion del optimo
    print(''.join(optimo))