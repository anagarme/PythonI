# Manejo de secuencias

#### Autor: Ana Marisol García Mejía
#### Actualización: 25/11/2023

## Introducción
Las tecnologías de secuenciación de nueva generación (_Next Generation Sequencing_) han revolucionado el campo de la genómica, permitiendo la secuenciación masiva de una gran variedad de genomas en poco tiempo. Sin embargo, trae consigo un reto importante, el manejo e interpretación de las secuencias en los formatos correspondientes. Por ejemplo, el formato FASTQ. Éste contiene el identificador de la secuencia, las lecturas y su puntuación de calidad, la cual está codificada con un único carácter ASCII. Este valor es muy importante  porque indica la confianza de la lectura y da mayor certeza a los análisis bioinformáticos. 

### Problema
Crear un programa que permita leer un archivo FASTQ y obtener el número de lecturas cuyo promedio de calidad está por debajo de un umbral dado.

## Metodología
1. Recibir desde línea de comandos la ruta del archivo FASTQ y el umbral de corte.
2. Leer el archivo FASTQ.
3. Iterar sobre las lecturas del archivo FASTQ. 
4. Calcular el promedio de calidad de cada una de las lecturas en el archivo.
5. Obtener el número de lecturas cuyo promedio de calidad está por debajo del umbral especificado.
7. Imprimir el número de lecturas. 

### Ejemplo 

```
py qualityFASTQS.py -f ..\data\sample.fastq -t 30
```

Output:
```
El número de lecturas con promedio de calidad por debajo del umbral 30 es: 5
```

## Resultados
El programa puede ser consultado en [mi repositorio de GitHub](https://github.com/anagarme/PythonI/tree/bfe657b5936511276ad799875bc34369fa8ba2a6/PythonClass/qualityFASTQS) 