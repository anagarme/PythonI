'''
NAME
       ContenidoAT_CG.py

VERSION
        1.0

AUTHOR
        Ana Marisol García Mejía

DESCRIPTION
        Este programa permite al usuario calcular el porcentaje de AT y CG en una secuencia de DNA, la cual es obtenida mediante 
        la lectura de un archivo de texto introducido por teclado. 

CATEGORY
        Genómica
USAGE

    % python ContenidoAT_CG.py
    
ARGUMENTS

METHOD

SEE ALSO
       
'''
# ===========================================================================
# =                            main
# ===========================================================================

# Explicar al usuario la utilidad del programa
print('¡Hola! \nEste programa te permite calcular el porcentaje de AT y CG en una secuencia de DNA, la cual es extraída de un archivo .txt')

# Pedir al usuario que introduzca la ruta del archivo .txt
my_file_name = input('Por favor, introduce la dirección de tu archivo: ')

# Acceder al archivo
with open(my_file_name,'r') as my_file:

    # Leer el archivo
    secuenciaDNA = my_file.read()

    # Quitar los saltos de línea con el método rstrip
    secuenciaDNA = secuenciaDNA.rstrip("\n")

    # Obtener la longitud de la secuencia 
    tamaño_dna = len(secuenciaDNA)

    # Sacar el total de AT y CG contenida en la secuencia de DNA con el método count
    AT = (secuenciaDNA.count('A') + secuenciaDNA.count('T'))
    CG = (secuenciaDNA.count('C') + secuenciaDNA.count('G'))

    # Calcular el porcentaje tanto de AT como CG
    porcentaje_AT = ((AT/tamaño_dna) * 100)
    porcentaje_CG = ((CG/tamaño_dna) * 100)

    # Imprimir en pantalla los porcentajes obtenidos
    print(f'El porcentaje de AT es: {porcentaje_AT} y el porcentaje de CG es: {porcentaje_CG}')
