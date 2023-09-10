'''
NAME
       conteo_bases.py

VERSION
        1.0

AUTHOR
        Ana Marisol García Mejía

DESCRIPTION
        Este programa permite obtener el total de cada base (A,T,C,G) en una secuencia de DNA dada por el usuario.

CATEGORY
        Genómica
USAGE

    % conteo_bases.py
    
ARGUMENTS

METHOD

SEE ALSO
       
'''
# ===========================================================================
# =                            main
# ===========================================================================


# Explicar al usuario la finalidad del programa 
print('¡Hola! Este programa te permite conocer la cantidad de cada base contenida en una secuencia de DNA dada.')

# Pedir al usuario la secuendia de DNA
secuenciaDNA = input('Por favor, introduce la secuencia de DNA: ')

# Contar el número de veces en las que aparece cada base en la secuencia con el método count
A = secuenciaDNA.count('A')
T = secuenciaDNA.count('T')
C = secuenciaDNA.count('C')
G = secuenciaDNA.count('G')

# Imprimir el total de cada base
print(f"El total por base es: \n A = {A} \n T = {T} \n C = {C} \n G = {G}")
