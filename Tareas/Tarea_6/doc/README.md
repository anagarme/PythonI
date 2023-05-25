# T6. Juego piedra papel o tijera 

Autor: Ana Marisol García Mejía 
Última actualización: 07/05/2023
_____
### Introducción 
Este reporte muestra la solución de un problema planteado, el cual es escribir un script en el que se simule el juego de piedra, papel o tijera. El programa pide al usuario que introduzca el número de partidas así como las opciones de su elección en cada ronda del juego. Mediante aleatoriedad se decide quién gana. Este programa emplea ciclos y condicionales, los cuales son implementados en la programación para reducir el número de líneas en el script, asimismo para que sea más legible. 

### Metodología
El siguiente algoritmo es el que se siguió para realizar este script: 
1. Imprimir un mensaje de bienvenida y una breve explicación al usuario de lo que realiza el programa. 
2. El usuario introduce su nombre y el número de partidas que quiere jugar. 
3. Importar la librería *random* para que se seleccione al azar la elección de la computadora.
4. Crear la función *juego(rondas)*, la cual simula el juego de piedra papel o tijera. 
5. Crear un ciclo *while* para que el código se repita cuantas rondas quiera jugar el usuario.  
6. Utilizar un contador para que cuente las rondas y termine el ciclo. 
7. El usuario introduce la opción que prefiera. 
8. Emplear el método *lower()* para evitar que el usuario introduzca su opción en mayúsculas. 
9. Con condicionales se evalúa la opción introducida por el usuario y la elegida aleatoriamente por la computadora. 
10. Tomar en cuenta  en cada caso el empate y las opciones de piedra vs tijera, papel vs tijera y piedra vs papel. 
11. Llamar a la función *juego()* y pasar el argumento *partidas*, que es el número de partidas que el usuario ingresó. 


### Resultados
Los resultados se muestran en el repositorio PythonI en GitHub. Consulta mi [repositorio](https://github.com/anagarme/PythonI/blob/4f1be4c120a64bc40fda88c78aa607f438ea4f87/Tareas/Tarea_6/src/piedra-papel-tijera.py).
