# T1. Git y GitHub:  add, commits
Ana Marisol García Mejía 
### Introducción 
En la actualidad los programas informáticos son de gran utilidad para realizar una infinidad de procesos que simplifican tareas rutinarias. Para ello se desarrollan códigos fuente, los cuales atraviesan una serie de modificaciones y mejoras hasta obtener un programa funcional y eficiente. Sin embargo, al modificar un código se requiere de una documentación detallada para saber exactamente cuáles cambios se realizaron, quién lo hizo y cuándo. Ante esta necesidad surgen los controladores de versiones como Git que nos permite mantener un registro de las actualizaciones del código, permitiendo así regresar a una etapa temprana de nuestro código o incluso permite trabajar en paralelo con otros programadores. 
### Metodología

```
# Revisamos la ruta del directorio donde nos encontramos 
pwd 
# Nos dirijimos al directorio PythonI donde crearemos nuestra carpeta
# Dentro de esta crear la carpeta projects, a su vez creamos el directorio reverse-complement
mkdir projects
cd projects
mkdir reverse-complement 
cd reverse-complement 
# Crear la estructura data docs src lib dentro de reverse-complement
mkdir data doc src lib
# Volver al directorio principal (PythonI)
cd ../../
# Inicializar el repositorio
git init
# Redirigirse a data
cd projects/reverse-complement/data/
# Abrir el editor de texto nano y crear el archivo donde se guardará la secuencia del gen araC de E. coli y agregar dicha secuencia de la base RegulonDB
nano E_coli_K12_araC.txt
# Ordena a Git que controle el archivo recién creado
git add E_coli_K12_araC.txt 
# Confirmar los cambios realizados y agregar un mensaje
git commit -m "Crear el archivo E_coli_K12_araC.txt"
# Moverse a la carpeta src 
cd ../
cd src
# Copiar el programa reverse-complement.py
cp /c/Users/Solecito/Documents/data-git/reverse-complement.py .
# Realizar el respectivo git add y commit a este programa 
git add reverse-complement.py
git commit -m "Agregando el archivo reverse-complement.py"
# Revisar el estado del repositorio
git status 
# Agregar el archivo README a doc y controlarlo por Git
cp /d/CienciasGenomicas/Semestre2023-2/Python/README.md .
git add README.md
git commit -m "Copiar el archivo README.md al repositorio doc"
# Vincular los commits realizados a GitHub
git remote add origin https://github.com/anagarme/PythonI.git
# Revisar si es correcta la dirección 
git remote -v 
# Exportar a GitHub todos los commits realizados
git push origin master 
# Por último se modificó el archivo README.md en GitHub, para traer estos cambios a nuestro controlador remoto se ejecutó: 
git pull origin master  

```

### Resultados 
Los resultados se muestran en el repositorio PythonI en GitHub. Para más información consultar mi repositorio https://github.com/anagarme/PythonI.git
