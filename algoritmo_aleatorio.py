import matplotlib.pyplot as plt
import osmnx as ox
import random 

def main_algoritmo_aleatorio(grafo, G , lista_pares_puntos, presupuesto, costo_metro):
    """
    Este algoritmo va simplemente a invertir en las vias aleatoriamente.
    
    Recibe: 
    
    1) grafo, este es un tipo de grafo en forma de diccionario 
    
    {(nodo1, nodo2), tiempo_en_recorrer}

    La tupla "la llave" esta sorteada, como los grafos internamente le ponen un numero a cada nodo del grafo
    entonces la forma correcta de representar las aristas es ver los nodos que conecta, se pone el tiempo en 
    recorrer como el valor de la llave ya que esto servira mas que los metros

    2) G, el grafo original, no sera de mucha utilidad ya que los algoritmos de distancias cortas y de caminos se 
    ejecutan en el otro formato

    3) Lista_nodos, son los pares de puntos que se seleccionan aleatoriamente segun la eleccion del usuario.
    Por ejemplo [(nodo1, nodo2), (nodo3, nodo4), ...] nodo1 y 2 representarian la casa y el trabajo del ciudadano 1
    y asi sucesivamente.

    4) Presupuesto, el dinero con el que se cuenta

    5) Costo por via, parametro relacionado con el presupuesto que determinara la cantidad de via disponible a mejora.

    Retorna:

    Lista de arista para optimizar las calles, posteriormente se hace la simulacion de que tanto mejoro la movilidad y 
    se presentan los resultados.
    
    """
    lista_puntos_invertidos = []
    metros_disponibles = presupuesto / costo_metro
    lista_disponibles = [nodos for nodos, metros in grafo.items() if metros <= metros_disponibles] 
    while len(lista_disponibles) > 0:
        arista_escogida = random.choice(lista_disponibles)
        lista_puntos_invertidos.append(arista_escogida)
        metros_disponibles -= grafo[arista_escogida]
        lista_disponibles = [nodos for nodos, metros in grafo.items() if metros <= metros_disponibles and nodos not in lista_puntos_invertidos] 

        print(f"Alcanzo para escoger esta via: {arista_escogida}")
    
    print("Se acabo el presupuesto para hacer mas vias, se seleccionaron estas: ", lista_puntos_invertidos)
    return lista_puntos_invertidos
