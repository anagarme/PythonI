my_file_name='C:/Users/LCG/Documents/PythonI/lessons/data/dna.txt'
my_file = open(my_file_name)
my_dna = my_file.read()
my_dna=my_dna.rstrip("\n")
dna_length=len(my_dna)
print("La secuencia es" + my_dna + "y su longitud es " + str(dna_length))


