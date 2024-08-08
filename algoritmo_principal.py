import osmnx
from dependencias import busqueda_recursiva, puntuacion

def algoritmo_principal(grafo, pares_puntos, presupuesto, costo_por_metro):
    caminos_usados = []
    contador_tiempo = 0
    contador_pares = 0 
    for salida, destino in pares_puntos():
        contador_pares = 0
        camino_mas_corto, distancia_optima = busqueda_recursiva(nodo_actual = inicio, nodo_objetivo= destino, grafo = grafo, visitados = [], camino = [inicio], distancias = [] )
