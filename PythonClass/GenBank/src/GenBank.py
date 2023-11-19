'''
NAME
   GenBank.py

VERSION 1.0 

AUTHOR
      Ana Marisol García Mejía

DESCRIPTION
     El programa recibe un archivo GenBank, el cual lo parsea para obtener
     información importante como la fecha, organismo, país y fuente del aislado.
     Además, recibe el nombre de un gen y devuelve la secuencia, el transcrito y 
     la traducción de dicho gen.
    
CATEGORY
    GenBank

USAGE
    % py GenBank.py [-h] [file] [gene]

ARGUMENTS
    -f FILE, --file FILE    Ruta al archivo con formato GenBank
    -g GENE, --gene GENE    Gen que se desea consultar

EXAMPLE
    % py GenBank.py -f virus.gb -g M
    
'''
# ===========================================================================
# =                            imports
# ===========================================================================
import argparse
from Bio import SeqIO

# ===========================================================================
# =                            parser
# ===========================================================================

parser = argparse.ArgumentParser(description="Parsea un archivo GenBank para obtener sus registros, secuencia de un gen, transcrito y proteína.\n")
parser.add_argument('-f','--file', type = str, help ="Ruta al archivo con formato GenBank")
parser.add_argument('-g', '--gene', type = str, help = "Gen que se desea consultar")

args= parser.parse_args()

# ===========================================================================
# =                            functions
# ===========================================================================

#Obtener los metadatos y features
def archivo_genbank(gb_file, gene):
    for gb_record in SeqIO.parse(gb_file, format="genbank"): 
        print(f"Fecha: {gb_record.annotations['date']}\n"      
            f"Organismo: {gb_record.annotations['organism']}\n"
            f"País: {gb_record.features[0].qualifiers['country']}\n"
            f"Fuente de aislado: {gb_record.features[0].qualifiers['isolation_source']}")

# Obtener la secuencia, el transcrito y la proteína    
        for feature in gb_record.features:
           if feature.type == 'gene' and feature.qualifiers['gene'][0] == args.gene:
                print(f"Gen:  {feature.qualifiers['gene']}\n")
                print(f"Secuencia DNA:\n{gb_record.seq[feature.location.start : feature.location.end]}\n")
                print(f"Transcripción:\n{gb_record.seq[feature.location.start : feature.location.end].transcribe()}\n")
                print(f"Traducción:\n{gb_record.seq[feature.location.start : feature.location.end].translate()}\n")



# ===========================================================================
# =                            main
# =========================================================================== 

gb_file = args.file
gene =args.gene

archivo_genbank(gb_file, gene)

