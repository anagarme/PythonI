'''
NAME
       convertir_a_FASTA.py

VERSION
        1.0

AUTHOR
        Ana Marisol García Mejía

DESCRIPTION
        Este programa permite al usuario  

CATEGORY
        Genómica
USAGE

    % python convertir_a_FASTA.py
    
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

# Escribir en el nuevo archivo el ID y la secuencia de DNA
fasta_file.write (f">ID_secuencia Especie\n {dna_txt}")

# Cerrar el archivo
fasta_file.close()

# Comprobar la existencia del archivo FASTA
my_fasta_file = 'C:/Users/qwerty/Documents/PythonI/lessons/src/dna.fasta'
my_fasta = open(my_fasta_file)
fasta = my_fasta.read()
print(fasta)