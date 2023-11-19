# Obtener información de las anotaciones y features
____
#### Autor: Ana Marisol García Mejía
#### Actualización: 18/11/2023
______

## Introducción
GenBank es una base que alberga la información genética y proteínas de diversas especies. Los archivos de este tipo de formato siguen una estructura bien definida que permite automatizar su consulta. Principalmente se divide en metadatos, que brinda información detallada sobre el organismo y del archivo por sí mismo; _features_, en la que se contiene las características de la secuencia, CDS, etc; y por último,  _origin_, que es la secuencia (DNA o proteína). 
### Problema
Crear un programa que permita leer un archivo GenBank y obtener información relevante de las anotaciones y features del archivo como el organismo del que proviene, la fecha, el país y la fuente de aislado.

## Metodología
1. Recibir desde línea de comandos la ruta del archivo GenBank. 
2. Parsear el contenido del archivo dado.
3. Iterar sobre los _records_ y sobre _annotations_ y _features_.
4. Obtener la fecha y nombre del organismo desde _annotations_.
5. Obtener el país y fuente de aislado desde _features_.

### Ejemplo 

```
py AnnotationsGenBank.py -f ..\data\virus.gb
```

Output:
```
Date: 13-AUG-2018
Organism: Isfahan virus
Country: ['Iran:Isfahan province']
Isolation source: ['Phlebotomus papatasi']

```

## Resultados
El programa puede ser consultado en [mi repositorio de Github](https://github.com/anagarme/PythonI/tree/53b65ba31201c748785a9193da9d3dccb91b6078/PythonClass/AnnotationsGenBank)
