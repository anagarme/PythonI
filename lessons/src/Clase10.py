## Clase 10 Python 
# 13.04.2023
# Programa de búsqueda
'''
archivo = open("data/out_a.txt", "w")
archivo2 = open("data/out_bh.txt", "w")

# Para buscar que empiece con a
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        archivo.write (accession + "\n")
    else:
        # accession.startswith('b' or 'h')
        archivo2.write (accession + "\n")

''' 
try:
    f = open('data/7-file_num.txt')
    my_number = int(f.read())
    print(my_number + 5)
except IOError as ex:
    print("sorry, couldn't open the file: " + ex.strerror)
except ValueError:
    print("sorry, couldn't parse the number") 