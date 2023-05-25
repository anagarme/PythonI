# =========================================================
#                          LISTAS
# =========================================================

"""
apes = ["Pongo pygmaeus", "Pan troglodytes", "Gorilla gorilla"]
conserved_sites = [24, 56, 132] 
#print(id(apes))
#print(id(conserved_sites))
#print(type(apes))
# print(apes[2])
#first_site = conserved_sites[2]

#print(apes[-1])
#print("tamaño ", len(apes))
#print("There are " + str(len(apes)) + " apes")
#print(apes[::])
monkeys = ["Papio ursinus", "Macaca mulatta"] 
primates = apes + monkeys

print(str(len(apes)) + " apes")
print(str(len(monkeys)) + " monkeys")
print(str(len(primates)) + " primates")
print(primates)


#print(apes.index("Pongo pygmaeus"))
primates.append("Pan paniscus")

print(primates)
#conserved_sites.extend([567, 34])
#print(conserved_sites)
"""
# =========================================================
#                          LOOPS
# =========================================================

#pes = ["Pongo pygmaeus", "Pan troglodytes", "Gorilla gorilla"] 

#for ape in apes: 
#   print(ape + " is an apen", end = "\t")
"""
apes = ["Pongo pygmaeus", "Pan troglodytes", "Gorilla gorilla"]
for ape in apes:
    name_length = len(ape)
    first_letter = ape[0]
    print(ape + " is an ape. Its name starts with " + first_letter)
    print("Its name has " + str(name_length) + " letters")  
"""      
                                                                                                                                                                                       
names = "melanogaster,simulans,yakuba,ananassae"
species = names.split(",")
print(species)
# recorremos la lista
for specie in species:
  print(specie + " is an specie")

"""
file = open("data/dna_sequences.txt")
for line in file:
  print("Length: " + str(len(line))  +"; "+ line)
file.close()
"""

file = open("data/dna_sequences.txt")

all_lines = file.readlines()

file.close()

for line in all_lines:
  print("Length: " + str(len(line)) )

for line in all_lines:
  print(line[:5] ) 