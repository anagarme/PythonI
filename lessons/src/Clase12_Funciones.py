#print("Este programa calcula el contenido de AT de una secuecia de DNA dada.")
#secuencia_DNA = input("Introduce tu secuencia de DNA: ")
#redondeo = input("Introduce las cifras sifnificativas: ")

def get_at_content(dna, sig_figs): # declaramos una variable como argumento
    length = len(dna) 
    a_count = dna.upper().count('A') 
    t_count = dna.upper().count('T') 
    at_content = (a_count + t_count) / length 
    return round(at_content, sig_figs) 

#print(get_at_content("ATCG", 2))

assert get_at_content("ATGCNNNNN",2) == 0.5