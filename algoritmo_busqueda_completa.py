from dependencias import evaluacion_n_grafo


pares_de_puntos_global = []
def main_algoritmo_busqueda_completa(grafo, G , lista_pares_puntos, presupuesto, costo_metro):
    """
    Mediante uso de recursion, explorar todas las inversiones posibles y minimizar el tiempo de transporte
    
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
    se presentan los resultados."""    

    global pares_de_puntos_global

    pares_de_puntos_global = lista_pares_puntos

    metros_disponibles = presupuesto / costo_metro

    lista_puntos_invertidos, promedio_minimo = recu_busqueda(grafo, [] , metros_disponibles)

    return lista_puntos_invertidos, promedio_minimo


def recu_busqueda(grafo, seleccionados, metros_disponibles):
    lista_disponibles = [nodos for nodos, metros in grafo.items() if metros <= metros_disponibles and nodos not in seleccionados]
    if len(lista_disponibles) == 0:
        return seleccionados,  None
    
    else: 
        mini = float(INF)
        lista_seleccion = list()
        for disponible in lista_disponibles:
            lista, promedio_viaje = recu_busqueda(grafo = grafo,seleccionados= seleccionados + disponible,metros_disponibles= metros_disponibles - grafo[disponible])
            if promedio_viaje is None:
                promedio_viaje = evaluacion_n_grafo(grafo, lista, pares_de_puntos_global)
            
            if promedio_viaje < mini:
                mini = promedio_viaje
                lista_seleccion = lista
            
        return lista_seleccion, mini

    

    