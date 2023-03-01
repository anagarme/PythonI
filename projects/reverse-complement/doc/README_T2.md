# T2. Comparar versiones y restaurar archivos 
Ana Marisol García Mejía 
### Introducción
Git permite llevar un regitro de cada una de las modificaciones en un archivo plano. Para ello se ejecuta un _commit_, cada uno está identificado por un ID, es importante resaltar que sino se lleva a cabo el _commit_ no es posible restaurar una versión. 

### Metodología
```
# Acceder al directorio data contenido en reverse-complement 
cd PythonI/projects/reverse-complement/data/ 
# Abrir el editor de textos nano para editar el archivo E_coli_K12_araC.txt
nano E_coli_K12_araC.txt
# Ordenar a Git que controle el archivo modificado y confirmar los cambios realizados
git add E_coli_K12_araC.txt
git commit -m "Se agregó la secuencia del gen araB"
# Simular una mutación en el gen araC, para ello se editará en nano
nano E_coli_K12_araC.txt 
# Confirmar los cambios en los nucleótidos
git add E_coli_K12_araC.txt 
git commit -m "Mutación en el gen araC"
# Comparar los archivos: última vs penútima y última vs antepenúltima.
# Para ello primero se obtuvieron los ID de los commits modificando dicho archivo. 
git log --oneline 
# Última vs penútima:
git diff 272cd5a 545eb12
git diff HEAD~1 E_coli_K12_araC.txt
# Última vs antepenúltima
git diff 272cd5a 89dee77
git diff HEAD~6 E_coli_K12_araC.txt 
# Restaurar la versión del archivo que no tiene las mutaciones. 
git checkout 545eb12 E_coli_K12_araC.txt
# Confirmar los cambios realizados
git add E_coli_K12_araC.txt
git commit -m "Restauración de la versión 2.0 de E_coli_K12_araC.txt"
# Comparar que los cambios sí se hayan hecho, esto con la versión actual y con la versión con mutaciones
git diff 7ed5cec 272cd5a
git diff HEAD~1 E_coli_K12_araC.txt
# Confirmar que no haya modificaciones sin guardar 
git status
# Agregar el archivo README_T2 a la carpeta data 
git add README_T2.md
git commit -m "Agragando reporte de la tarea 2"
# Exportar a GitHub todos los commits realizados
git push origin master

```
### Resultados 
Los resultados se muestran en el repositorio PythonI en GitHub. Para más información consultar mi repositorio https://github.com/anagarme/PythonI.git