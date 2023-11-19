# Obtener la secuencia de un gene de un archivo GenBank

#### Autor: Ana Marisol García Mejía
#### Actualización: 18/11/2023


## Introducción
Los archivos GenBank al poseer un formato estándar permiten automatizar los procesos de búsqueda. Es por ello que es posible obtener la secuencia de un gene o proteína de interés a través de un programa. Además, las librerías de Biopython permiten aplicar atributos a las secuencias y hacer más sencillo su manejo. 

### Problema
Crear un programa que permita obtener la secuencia de un gene de interés, además, que devuelva el transcrito, la proteína que codifica, así como información importante del archivo GenBank.

## Metodología
1. Recibir desde línea de comandos la ruta del archivo GenBank y el gene que se desea consultar
2. Iterar sobre los _records_ del archivo.
3. Iterar sobre los _features_ del objeto para buscar el gene deseado.
4. Buscar si el gene objetivo se encuentra en el archivo.
5. Imprimir el nombre del gene, la secuencia, el transcrito y la proteína de éste.

### Ejemplo 

```
py GenBank.py -f ..\data\virus.gb -g M
```

Output:
```
Fecha: 13-AUG-2018
Organismo: Isfahan virus
País: ['Iran:Isfahan province']
Fuente de aislado: ['Phlebotomus papatasi']
Gen:  ['M']

Secuencia DNA:
ATGAAGAG...GCTATTGA
Transcripción:
AUGAAGAG...GCUAUUGA
Traducción:
MKSLKRLI...TWLISKSY

```

## Resultados
El programa puede ser consultado en [mi repositorio de GitHub](https://github.com/anagarme/PythonI/tree/53b65ba31201c748785a9193da9d3dccb91b6078/PythonClass/GenBank) 