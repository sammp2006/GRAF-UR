import osmnx
from dependencias import busqueda_intermedia, puntuacion

def main_algoritmo_principal(grafo, G , lista_pares_puntos, presupuesto, costo_metro):
    """
    Este algoritmo es el mas elaborado de los 4 y consiste en un metodo de evaluacion que busca no tener
    unicamente en cuenta la concurrencia de las vias sino tambien la proximidad de ciertas rutas entre si para 
    buscar "unirlas", similar a como se construyen autopistas. La idea es que este algoritmo sea una extension del
    llamado algoritmo "simple". Sin embargo, la respuesta que arroje siempre sera superada tanto en tiempo como
    en resultado por la busqueda completa, que se mantiene varios ordenes de complejidad por encima.

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
    
    
    caminos_usados = []
    contador_tiempo = 0
    contador_pares = 0 
    for salida, destino in pares_puntos():
        contador_pares += 1
        camino_mas_corto, distancia_optima = busqueda_intermedia(nodo_actual = inicio, nodo_objetivo= destino, grafo = grafo, visitados = [], camino = [inicio], distancias = [] )
        caminos_usados += camino_mas_corto
        contador_tiempo += distancia_optima