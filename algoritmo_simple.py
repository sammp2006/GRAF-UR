
def main_algoritmo_simple(grafo):
    """
    Este algoritmo solo toma en cuenta la concurrencia actual de las carreteras para hacer inversiones
    
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
    

    
    pass