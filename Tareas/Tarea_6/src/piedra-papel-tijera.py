'''
NAME
       piedra-papel-tijera.py

VERSION
        1.0

AUTHOR
        Ana Marisol García Mejía

DESCRIPTION
        Este programa es una representación del clásico juego piedra, papel o tijera. 
        El usuario puede jugar las partidas que establezca y su oponente será el ordenador
        (y la aleatoriedad). 

CATEGORY
        Entretenimiento
USAGE

    % python piedra-papel-tijera.py
    
ARGUMENTS
    El argumento rondas de la función juego es el número de partidas que el usuario decide jugar. 

METHOD

SEE ALSO
       
'''


# ===========================================================================
# =                            imports
# ===========================================================================
import random

# ===========================================================================
# =                            functions
# ===========================================================================

def juego(rondas):
    """
    Función que simula el juego de papel, piedra y tijera. El jugador introduce la opción que prefiera, entonces el ordenador por aleatoriedad
    elige su opción.

    Args: 
    rondas = Es el número de partidas que el usuario decide jugar. En cada iteración se elige una opción diferente. 

    """
    # El ciclo while se implementó para repetir el juego cuantas veces el usuario desee.
    partida = 0
    while partida < partidas:  
        partida += 1 
    # Las opciones que puede elegir el método random
        opciones = ['piedra', 'papel', 'tijera']
    
    # Elección del ordenador mediante aleatoriedad con el método random
        pc = random.choice(opciones)
    
    # El usuario introduce su opción 
        jugador = input(f"{nombre} elige piedra, papel o tijera: ")
    
    # Se emplea el método lower para evitar un error al momento de que se interprete y compare las elecciones
        humano = jugador.lower()
    
    # Caso en el que el ordenador y el jugador elijan la misma opción
        if pc == jugador:
            print("¡Empate!")
    
    # Se toman en cuenta cada caso fuera del empate
        elif pc == "piedra" and humano == "tijera":
            print("¡Elegí piedra! Gané :)")
        if pc == "tijera" and humano == "piedra":
            print(f"¡Elegí tijera! Ganaste, {nombre} <3")
        elif pc == "papel" and humano == "tijera":
            print("¡Elegí papel! Ganaste :)") 
        if pc == "tijera" and humano =="papel":
                print("¡Elegí tijera! Gané :)")
        elif pc == "papel" and humano == "piedra":
            print ("¡Elegí papel! Gané :)")
        if pc == "piedra" and humano == "papel":
            print("¡Elegí piedra! Ganaste <3")
    
# ===========================================================================
# =                            main
# ===========================================================================

# Bienvenida y explicación del juego 
print("Bienvenido al clásico juego de piedra, papel o tijera.")
nombre = input("¿Cuál es tu nombre? ")

print(f'Las reglas son sencillas, {nombre}, sólo debes introducir el número de partidas y tu opción. ')
partidas = int(input("Introduce el número de partidas: "))

# Se llama a la función y se pasa el argumento partidas 
juego(partidas)
   



