from dependencias import busqueda_intermedia, algoritmo_voraz
# from dependencias import busqueda_recursiva, algoritmo_voraz

def main_algoritmo_simple(grafo, G , lista_pares_puntos, presupuesto, costo_metro):
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

    diccionario_concurrencia = {}

    for par in lista_pares_puntos:
        camino, distancias = busqueda_intermedia(grafo_viejo = grafo, inicio= par[0], objetivo= par[1])
        print(camino, distancias)
        for el in camino:
            if diccionario_concurrencia.get(el) is None:
                diccionario_concurrencia[el] = 1
            else:
                diccionario_concurrencia[el] += 1

        print(diccionario_concurrencia)

    vias_mejorar = algoritmo_voraz(puntajes=diccionario_concurrencia, G = G, presupuesto= presupuesto)

    return vias_mejorar
    