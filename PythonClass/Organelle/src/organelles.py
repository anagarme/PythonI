'''
NAME
   organelles.py

VERSION 1.0 

AUTHOR
      Ana Marisol García Mejía

DESCRIPTION
     
    
CATEGORY
    Biology

USAGE
    % py organelles.py [-h] [-o ORGANELLE] [-p PRODUCTION]

ARGUMENTS
    -o ORGANELLE, --organelle ORGANELLE         Organelo que debe empezar la síntesis: nucleo o mitocondria únicamente
     -p PRODUCTION, --production PRODUCTION     Capacidad de producción de las biomoléculas: alta, media o baja

EXAMPLE
    % py organelles.py -o nucleo -p alta
    

'''
# ===========================================================================
# =                            imports
# ===========================================================================

import argparse
parser = argparse.ArgumentParser(description="Simula la síntesis del material genético y de ATP en una célula eucariota\n")
parser.add_argument('-o','--organelle', type = str, help ="Organelo que debe empezar la síntesis: nucleo o mitocondria (únicamente)")
parser.add_argument('-p', '--production', type=str, help='Capacidad de producción de las biomoléculas: alta, media o baja')

args= parser.parse_args()

# ===========================================================================
# =                            functions
# ===========================================================================
class Organelo():
    def __init__(self, nombre):
        self.nombre = nombre

    def signaling(self):
        print(f'Realizando vía de señalización para la supervivencia del organelo {self.nombre}')
    def realizar_funcion(self):
        print(f'Realizando función del organelo {self.nombre}...')


class Nucleo(Organelo):
    def __init__(self, nombre, tasa_replicacion):
        super().__init__(nombre)
        self.tasa_replicacion = tasa_replicacion

    def realizar_funcion(self):
        print(f"Replicando el material genético en el {self.nombre}")
        print(f"La tasa de replicación del DNA es {self.tasa_replicacion}")


class Mitocondria(Organelo):
    def __init__(self, nombre, produccion_ATP):
        super().__init__(nombre)
        self.produccion_ATP = produccion_ATP

    def realizar_funcion(self):
        print(f"Generando energía en la {self.nombre}")
        print(f"Capacidad de producción de ATP: {self.produccion_ATP}")


# ===========================================================================
# =                            main
# ===========================================================================  
# Crear instancias de las clases

organelle = args.organelle
production = args.production

nucleo_celular = Nucleo(organelle, production)
mitocondria_celular = Mitocondria(organelle, production)

# Llamadas a los métodos

print("Célula sintetizando...")
if args.organelle == 'mitocondria':
    mitocondria_celular.realizar_funcion()
    nucleo_celular.realizar_funcion()
else:
    nucleo_celular.realizar_funcion()

