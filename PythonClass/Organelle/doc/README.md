# Simulación de la síntesis de DNA y ATP en una célula eucariota

#### Autor: Ana Marisol García Mejía
#### Actualización: 19/11/2023

## Introducción
Las células eucariotas cumplen con diversas funciones para su propia supervivencia, es así que requieren sintetizar biomoléculas como el material genético y ATP. Más importante es que cada función la lleva a cabo en un organelo específico.

### Problema
Crear un programa que permita que tenga al menos una clase y al menos 2 métodos. Se debe aplicar la herencia, el _overriding_ y polimorfismo.

## Metodología
1.  Recibir desde línea de comandos el organelo (núcleo o mitocondria) y la tasa de producción (alta, media o baja)
2. Crear la clase padre Organelo. 
3. Llamar al constructor. 
4. Crear dos métodos de la clase padre.
5. Aplicar el _overriding_.
6. Crear instancias de las clases.

### Ejemplo 
Caso 1: Mitocondria
```
py organelles.py -o mitocondria -p alta
```

Output:
```
Célula sintetizando...
Generando energía en la mitocondria
Capacidad de producción de ATP: alta

```

Caso 2: Núcleo 
```
py organelles.py -o nucleo -p media
```


Output: 
```
Célula sintetizando...
Replicando el material genético en el nucleo
La tasa de replicación del DNA es media

```
## Resultados
El programa puede ser consultado en [mi repositorio de Github](https://github.com/anagarme/PythonI/tree/24e9d5e920b612eeefb8c1194192275ecfc0540b/PythonClass/Organelle)
