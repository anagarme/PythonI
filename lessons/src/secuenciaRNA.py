'''
NAME
       secuenciaRNA.py

VERSION
        1.0

AUTHOR
        Ana Marisol García Mejía

DESCRIPTION
        Este programa permite obtener la posición del codón de inicio y del codón de término en una secuencia de DNA,
        además imprime el fragmento de DNA que será transcrita en RNA. 

CATEGORY
        Genómica
USAGE

    % python secuenciaRNA.py
    
ARGUMENTS

METHOD

SEE ALSO
       
'''
# ===========================================================================
# =                            main
# ===========================================================================

# Secuencia de DNA en la que se buscará el codón de inicio y de término
dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'

# Almacenar el codón de inicio
codon_inicio = 'TAC'

# Almacenar el codón de término 
codon_paro = 'ATT'

# Buscar en la secuencia con el método find los codones de inicio y término respectivamente 
inicio = dna.find(codon_inicio)
final = dna.find(codon_paro)

# Imprimir las posiciones de los codones de inicio y final
print(f'El codón de inicio (TAC) se encuentra en la posición: {inicio}\n El codón de paro (ATT) está en la posición: {final}')

# Extraer la secuencia de DNA que será transcrita 
mRNA = dna[inicio:final]

# Imprimir la secuencia de DNA que será transcrita en RNA
print(f'El fragmento de DNA que será trasncrito es: {mRNA}')