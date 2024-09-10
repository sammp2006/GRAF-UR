# Proyecto-Final GRAF-UR
Proyecto Final Introducción a las Ciencias de la Computación (2024 I)

# GRAF-UR

*GRAF-UR* es un programa en Python con interfaz gráfica que propone una solución a los embotellamientos en las calles de varias ciudades de Colombia. Utilizando técnicas de simulación, permite al usuario estimar mejoras en la movilidad de acuerdo con un presupuesto de inversión en carreteras.

## Descripción

El programa permite al usuario seleccionar una ciudad disponible y visualizar su mapa en forma de grafo. Luego, el usuario ingresa un presupuesto, representado en "metros de carretera" a mejorar, y el programa calcula el tiempo estimado para viajar de un punto A a un punto B bajo diferentes escenarios de mejora:

1. *Sin mejoras*: Calcula el tiempo estimado con las condiciones actuales de las vías.
2. *Simulación simple / voraz*: Prioriza la mejora de las calles más transitadas.
3. *Simulación aleatoria*: Mejoras aplicadas aleatoriamente, con resultados inciertos.
4. *Búsqueda completa*: Analiza exhaustivamente todas las posibles inversiones y caminos (menos eficiente).

Este proyecto tiene como objetivo ayudar a evaluar cómo la inversión en infraestructura puede afectar el tráfico en ciudades colombianas.

## Instalación

Sigue estos pasos para instalar y ejecutar el programa:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/sammp2006/GRAF-UR.git
   
2. Entrar a la Carpeta:
   ```bash
   cd GRAF-UR
   
3. Instalar Dependencias:
   ```bash
   pip install -r dependencias.txt

4. Ejecutar:
   ```bash
   python3 run.py

## Uso
1.   Selecciona una de las ciudades disponibles en el menú.
2.   Introduce el número de "metros de carretera" que deseas mejorar.
3.   Escoge el algoritmo de simulación que deseas utilizar:
       Sin mejoras
    Simulación simple
    Simulación aleatoria
    Búsqueda completa
4.  El programa calculará el tiempo estimado de viaje de A a B bajo el escenario seleccionado.
## Ejemplo
Selecciona Bogotá y especifica un presupuesto de 2000 metros de carretera. Luego, selecciona la simulación simple. El programa mostrará el tiempo estimado de mejora en las principales calles mejoradas con el presupuesto asignado.
