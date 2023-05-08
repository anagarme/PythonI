'''
NAME
       T4_convertir_a_FASTA.py

VERSION
        1.0

AUTHOR
        Ana Marisol García Mejía

DESCRIPTION
        Este programa permite al usuario convertir un archivo .txt que contenga una secuencia de DNA en un archivo formato FASTA,
        el cual se guarda con extensión .fasta

CATEGORY
        Genómica
USAGE

    % python T4_convertir_a_FASTA.py
    
ARGUMENTS

METHOD

SEE ALSO
       
'''
# ===========================================================================
# =                            main
# ===========================================================================

# Explicar al usuario la utilidad del programa
print('¡Hola! \nEste programa te permite convertir un archivo .txt que contenga una secuencia de DNA en formato FASTA.')

# Pedir al usuario que introduzca la ruta del archivo .txt
my_file_name = input('Por favor, introduce la dirección de tu archivo .txt: ')

# Acceder al archivo
my_file = open(my_file_name)

# Leer el archivo
dna_txt = my_file.read()

# Abrir y crear un nuevo archivo con extensión .fasta
fasta_file = open("dna.fasta", "w")

# Pedir al usuario que introduzca el ID de su secuencia 
ID = input("Introduce el ID que quieres que tenga tu archivo FASTA")

# Escribir en el nuevo archivo el ID y la secuencia de DNA
fasta_file.write (f">{ID}\n{dna_txt}\n")

# Cerrar el archivo
fasta_file.close()

print('¡El archivo se creó exitosamente!')

# Comprobar la existencia del archivo FASTA
my_file_fasta = input('Si deseas corroborar que se creó introduce la dirección del archivo dna.fasta: ')

# Acceder al archivo FASTA
my_fasta = open(my_file_fasta)

# Leer el archivo
fasta = my_fasta.read()

# Imprimir en pantalla el contenido 
print(fasta)
