# Contenido de AT y GC 
Autor: Ana Margisol García Mejía 
Última actualización: 07/05/2023 
____

### Introducción
Los programas pueden recibir cadenas de caracteres, números enteros, etc. como datos requeridos para que el programa pueda funcionar o implementar los métodos para obtener la solución del problema. Sin embargo, también se suelen necesitar archivos de texto plano para que el programa funcione adecuadamente. Para ello, existen métodos que permiten abrirlos, modificarlos e incluso crearlos. 
En este reporte empleamos la lectura de archivos de texto plano para obtener el porcentaje de AT y CG en una secuencia de DNA dada en un archivo .txt introducido por el usuario. 

### Metodología 
1. Explicar al usuario la utilidad del programa.
2. Pedir al usuario que introduzca la ruta del archivo .txt 
3. Acceder y leer al archivo.
4. Quitar los saltos de línea con el método *rstrip("/n")*.
5. Obtener la longitud de la secuencia.
6. Calcular el total de AT y CG contenida en la secuencia de DNA con el método *count()* para cada una de las bases y almacenarlo en las variables *AT* y *CG* respectivamente.
7. Calcular el porcentaje tanto de AT como CG.
8. Imprimir en pantalla los porcentajes obtenidos.

#### Recomendación
En la carpeta *data* se encuentra un archivo llamado *[dna.txt](https://github.com/anagarme/PythonI/blob/cfb69b8423099267738b212f308b2b240d1769d0/Tareas/Tarea_3/data/dna.txt)*, el cual sirve para probar que el programa funciona correctamente. 


### Resultados
Los resultados se muestran en el repositorio PythonI en GitHub. Consulta mi [repositorio]( https://github.com/anagarme/PythonI/blob/7d69822bc83875b605ec41143df57272b20d97f7/Tareas/Tarea_3/src/ContenidoAT_CG.py). 