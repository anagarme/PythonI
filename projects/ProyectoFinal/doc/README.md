# Proyecto final
## Piedra, papel o tijera

Autor: Ana Marisol García Mejía
Última modificación: 25/05/2023

_____
### Introducción
Piedra, papel o tijera es un juego tradicional que se ha extendido por todo el mundo. Por lo general, se usa para poder tomar ciertas decisiones y, en algunos casos, se juega por diversión. Las reglas piden que los jugadores que compiten usen una mano para hacer una de las tres formas (piedra, papel o tijera) en el momento acordado. La persona que haya elegido la forma más fuerte es el ganador del [juego](https://es.wikihow.com/jugar-piedra,-papel-o-tijera). ¡Así de simple! 
Sin embargo, si quieres tomar una decisión importante y no tienes algún acompañante puedes optar por jugar con tu computadora mediante un sencillo programa como el implementado en este repositorio. 

________
### Requisitos
Para poder ejecutar el programa se requiere tener instalado el siguiente software: 
- Python version 3.9.2 o superior 
Asimismo, se debe importar la librería random, no obstante esta es importada al ejecutar el programa en la sección *Imports*.

_____
### Instalación 
El programa está escrito en Python. Por lo que debes seguir los siguientes pasos para instalarlo. 
1. Descargar o copiar el script en un archivo ***.py*** en una carpeta conocida. 
2. Ejecutar el programa en línea de comandos de tu computadora. Es importante destacar que al ejecutarlo se debe considerar la ruta absoluta donde se encuentra el programa.
```
python piedra-papel-tijera.py
```

____
### Funcionamiento del programa 
### Algoritmo 
El siguiente algoritmo es el que se siguió para realizar este script: 
1. Imprimir un mensaje de bienvenida y una breve explicación al usuario de lo que realiza el programa. 
2. El usuario introduce su nombre y el número de partidas que quiere jugar. 
3. Importar la librería *random* para que se seleccione al azar la elección de la computadora.
4. Crear la función *juego(rondas)*, la cual simula el juego de piedra papel o tijera. 
5. Crear un ciclo *while* para que el código se repita cuantas rondas desee jugar el usuario.  
6. Utilizar un contador para que cuente las rondas y termine el ciclo. 
7. El usuario introduce la opción que prefiera. 
8. Emplear el método *lower()* para evitar que el usuario introduzca su opción en mayúsculas. 
9. Con condicionales se evalúa la opción introducida por el usuario y la elegida aleatoriamente por la computadora. 
10. Tomar en cuenta  en cada caso el empate y las opciones de piedra vs tijera, papel vs tijera y piedra vs papel. 
11. Crear un ciclo *while* para ejecutar la función *juego* y que el usuario decida si continúa el juego o termina.
12. Llamar a la función *juego()* y pasar el argumento *partidas*, que es el número de partidas que el usuario ingresó. 

#### Ejemplos
¿Cómo funciona el programa?
Inicialmente el programa imprimirá en pantalla un mensaje de bienvenida y solicitará tu nombre. 
```
Bienvenido al clásico juego de piedra, papel o tijera.
¿Cuál es tu nombre? Ana
```
Una vez ingresado te explica las reglas y debes de ingresar el número de partidas. 
```
Las reglas son sencillas, Ana, sólo debes introducir el número de partidas y tu opción (papel, piedra, tijera).
Introduce el número de partidas: 3
```
El programa imprime en pantalla para que selecciones tu opción, puede ser ingresado en minúsculas o mayúsculas, pero es importante que sea la palabra completa. 
```
Sol elige piedra, papel o tijera: piedra
¡Elegí papel! Gané :)
Sol elige piedra, papel o tijera: PIEDRA
¡Elegí papel! Gané :)
```
Una vez terminado las partidas se imprime el siguiente mensaje para volver a ejecutar el programa: 
```
Ingresa 1 si deseas volver a jugar o 0 para cerrarlo: 1
```
Si el usuario ingresa 1 el programa se vuelve a ejecutar y realiza todos los pasos descritos anteriormente: 
```
Ingresa 1 si deseas volver a jugar o 0 para cerrarlo: 1 
Introduce el número de partidas: 
```
En caso contrario, si ingresa un 0 el programa se cierra e imprime un mensaje de despedida.
```
Ingresa 1 si deseas volver a jugar o 0 para cerrarlo: 0
Gracias por jugar conmigo, espero que te hayas divertido :)
```