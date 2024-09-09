from dependencias import evaluacion_n_grafo

pares_de_puntos_global = []

def main_algoritmo_busqueda_completa(grafo, G, lista_pares_puntos, metros_disponibles):
    """
    Mediante uso de recursion, explorar todas las inversiones posibles y minimizar el tiempo de transporte.
    
    Recibe:
    1) grafo: Diccionario de aristas {(nodo1, nodo2): tiempo_en_recorrer}
    2) G: Grafo original (no utilizado en este código)
    3) lista_pares_puntos: Lista de pares de puntos a considerar.
    4) presupuesto: Dinero disponible.
    5) costo_metro: Costo por metro de calle a mejorar.
    
    Retorna:
    Lista de aristas para optimizar y el promedio mínimo de tiempo de viaje.
    """
    
    global pares_de_puntos_global
    pares_de_puntos_global = lista_pares_puntos

    lista_puntos_invertidos, promedio_minimo = recu_busqueda(grafo, [], metros_disponibles)

    return lista_puntos_invertidos, promedio_minimo


def recu_busqueda(grafo, seleccionados, metros_disponibles):
    """
    Función recursiva para buscar la mejor combinación de aristas a seleccionar.
    
    Recibe:
    1) grafo: Diccionario de aristas {(nodo1, nodo2): tiempo_en_recorrer}
    2) seleccionados: Lista de aristas ya seleccionadas.
    3) metros_disponibles: Cantidad de metros disponibles para mejorar.
    
    Retorna:
    Lista de aristas seleccionadas y el promedio mínimo de tiempo de viaje.
    """
    
    lista_disponibles = [(nodos, metros) for nodos, metros in grafo.items() if metros <= metros_disponibles and nodos not in seleccionados]

    if not lista_disponibles:
        promedio_viaje = evaluacion_n_grafo(grafo, seleccionados, pares_de_puntos_global)
        return seleccionados, promedio_viaje
    
    mini = float("inf")
    lista_seleccion = []

    for disponible in lista_disponibles:
        nueva_seleccion, promedio_viaje = recu_busqueda(
            grafo, 
            seleccionados + [disponible[0]], 
            metros_disponibles - disponible[1]
        )
        
        if promedio_viaje is None:
            promedio_viaje = evaluacion_n_grafo(grafo, nueva_seleccion, pares_de_puntos_global)
        
        if promedio_viaje < mini:
            mini = promedio_viaje
            lista_seleccion = nueva_seleccion
    
    return lista_seleccion, mini

    