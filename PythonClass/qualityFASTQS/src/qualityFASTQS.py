'''
NAME
   qualityFASTQS

VERSION 1.0 

AUTHOR
      Ana Marisol García Mejía

DESCRIPTION
    
    El programa obtiene el número de lecturas cuyo promedio de calidad está debajo de un umbral dado por el usuario. 
    
        
USAGE
    % py qualityFASTQS.py [-h] [-f FILE] [-t THRESHOLD]

ARGUMENTS
    -f FILE, --file FILE                    Ruta al archivo FASTQ
    -t THRESHOLD, --threshold THRESHOLD     Umbral de corte 

EXAMPLE

    %py  qualityFASTQS.py -f sample.fastq -t 30
    
'''


# ===========================================================================
# =                            imports
# ===========================================================================
from Bio import SeqIO
import argparse

# ===========================================================================
# =                            parser
# ===========================================================================
parser = argparse.ArgumentParser(description="El programa obtiene el número de lecturas en un archivo FASTQ cuyo promedio de calidad está debajo de un umbral dado.\n")
parser.add_argument('-f', '--file', type = str, help = "Ruta al archivo con formato FASTQ")
parser.add_argument('-t', '--threshold', type = int, help = "Valor del umbral de corte")

args= parser.parse_args()


# ===========================================================================
# =                            functions
# ===========================================================================

def calidad_fastq(fastq_file, threshold):

    lecturas_bajo_umbral = 0
    for record in SeqIO.parse(fastq_file, "fastq"):
    # Calcular el promedio de calidad de las lecturas
        promedio_calidad = sum(record.letter_annotations["phred_quality"]) / len(record)
                
        # Revisar si el promedio de calidad está por debajo del umbral dado
        if promedio_calidad < threshold:
            lecturas_bajo_umbral += 1

    print(f"El número de lecturas con promedio de calidad por debajo del umbral {threshold} es: {lecturas_bajo_umbral}")
    

# ===========================================================================
# =                            main
# =========================================================================== 
fastq_file = args.file
threshold = args.threshold


calidad_fastq(fastq_file, threshold)

