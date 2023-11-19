'''
NAME
   AnnotationsGenBank.py

VERSION 1.0 

AUTHOR
      Ana Marisol García Mejía

DESCRIPTION
    El programa recibe un archivo GenBank y lo parsea para obtener 
    información de sus anotaciones y registros.

CATEGORY
    GenBank
        
USAGE
    % py AnnotationsGenBank.py [-h] [file]

ARGUMENTS
    -f FILE, --file FILE Ruta al archivo con formato GenBank


EXAMPLE
    py AnnotationsGenBank.py -f virus.gb

'''
# ===========================================================================
# =                            imports
# ===========================================================================
from Bio import SeqIO
import argparse

# ===========================================================================
# =                            parser
# ===========================================================================

parser = argparse.ArgumentParser(description="Imprime los registros de un archivo GenBank \n")
parser.add_argument('-f','--file', type = str, help ="Ruta al archivo con formato GenBank")
args= parser.parse_args()

# ===========================================================================
# =                            functions
# ===========================================================================

# Obtener los metadatos y features
def annottions_features(gb_file):
    for record in SeqIO.parse(gb_file, "genbank"):
        print(f"Date: {record.annotations['date']}\n"
            f"Organism: {record.annotations['organism']}\n"
            f"Country: {record.features[0].qualifiers['country']}\n"
            f"Isolation source: {record.features[0].qualifiers['isolation_source']}")

# ===========================================================================
# =                            main
# ===========================================================================

annottions_features(gb_file=args.file)