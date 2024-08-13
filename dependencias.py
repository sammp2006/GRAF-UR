import copy
import random
import numpy as np
import osmnx as ox
import heapq
import matplotlib.pyplot as plt


def importar_grafos(nombre):
    G = ox.graph_from_place(nombre, network_type= "drive")
    return G

def transformacion_grafo(G):
    """Recibe el grafo en formato OSMNX y lo retorna en una estructura de datos mas comoda
    
    retorna
    grafo: dict= {(nodo1, nodo2): distancia_metros, etc} la tupla (nodo1 y nodo2 esta ordenada)

    """
    nodos = G.nodes(data=True)
    aristas = G.edges(data=True)

    grafo = {}
    for inicio, fin, info in aristas:
        distancia = info["length"]
        llave = tuple(sorted([inicio, fin]))
        grafo[llave] = distancia
    return grafo

def color_aleatorio():
    """
    Para representar a los pares de puntos (los destinos y la casa) de los ciudadanos, escogemos un color
    aleatorio en formato hexadeciman (255,255,255) que matplotlib pueda entender
    
    """
    r = random.randint(0, 255)  # Paraa el Rojo
    g = random.randint(0, 255)  # Para el Verde
    b = random.randint(0, 255)  # Para el Azul
    
    color_hexa = f"#{r:02X}{g:02X}{b:02X}" # Formato hexadecimal 255 pasarlo a FF por ej
    
    return color_hexa #Retorno como string 

def elegir(nodos):
    """Selecciona un nodo aleatorio de la lista de nodos."""
    return random.choice(list(nodos))

def ver_grafo_con_puntos(G, lista_pares_nodos):
    """
    Muestra un grafo con nodos resaltados en las coordenadas especificadas.
    
    entradas:
    El grafo de OSMNX.
    la lista_pares_nodos: Lista de pares de IDs de nodos. Cada par representa un conjunto de nodos a resaltar.
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Plotear el grafo
    ox.plot_graph(
        G,
        node_size=10,
        node_color="lightgrey",
        edge_linewidth=1.0,
        edge_color="black",
        show=False,
        ax=ax
    )
    
    # Obtener las posiciones de los nodos
    pos = {node: (G.nodes[node]['x'], G.nodes[node]['y']) for node in G.nodes}
    
    # Resaltar los nodos
    i = 0
    for nodos in lista_pares_nodos:
        i += 1
        # Seleccionar un color aleatorio para cada conjunto de puntos
        color = color_aleatorio()
        # Extraer coordenadas de los nodos
        xs, ys = zip(*[pos[node] for node in nodos if node in pos])  
        # Plotear los puntos
        ax.scatter(xs, ys, color=color, s=100, label=f'Ciudadano # {i} identificado con: {color}', edgecolor='black')
    
    # Configurar el título y etiquetas de los ejes
    ax.set_title("Pares de puntos", fontsize=20)
    ax.set_xlabel("Longitud", fontsize=14)
    ax.set_ylabel("Latitud", fontsize=14)
    
    # Ajustar los límites de los ejes
    xlim = (min(pos[node][0] for node in G.nodes) - 0.01, max(pos[node][0] for node in G.nodes) + 0.01)
    ylim = (min(pos[node][1] for node in G.nodes) - 0.01, max(pos[node][1] for node in G.nodes) + 0.01)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    
    ax.legend()
    
    plt.show()
def ver_grafo(G, titulo):
    # Crear una figura y un eje
    fig, ax = plt.subplots(figsize=(10, 10))
    
    ox.plot_graph(
        G,
        node_size=10,  # Tamaño 
        node_color="gold",  # Color 
        edge_linewidth=1.5,  # Grueso
        edge_color="black",  # Color 
        show=False, # Para evitar que se salte sola la grafica
        ax=ax 
    )
    
    ax.set_title(f"{titulo}", fontsize=20)  # Cambia el título del gráfico aquí
    ax.set_xlabel("Longitud", fontsize=14)
    ax.set_ylabel("Latitud", fontsize=14)
    
    xlim = (min(G.nodes[node]['x'] for node in G.nodes) - 0.01, max(G.nodes[node]['x'] for node in G.nodes) + 0.01)
    ylim = (min(G.nodes[node]['y'] for node in G.nodes) - 0.01, max(G.nodes[node]['y'] for node in G.nodes) + 0.01)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    
    plt.show()

def distancia_euclidiana(x1, y1, x2, y2):
    """
    Distancia euclidiana o teorema de pitagoras para dos pares de puntos
    """
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def distancia_punto_segmento(x1, y1, x2, y2, xp, yp):
    """
    Distancia de un punto a un segmento
    """
    try:
        m = (y1 - y2) / (x1 - x2)
        b = y1 - m * x1

        m_perpendicular = -(1 / m)
        b_perpendincular = yp - m_perpendicular * xp

        xi = (b - b_perpendincular) / (m_perpendicular - m)
        yi = m * xi + b

        max_x = max(x1, x2)
        min_x = min(x1, x2)
        if xi > min_x and xi < max_x:
            distance = distancia_euclidiana(xi, yi, xp, yp)
        elif xi > max_x:
            max_y = m * max_x + b
            distance = distancia_euclidiana(max_x, max_y, xp, yp)
        else:
            min_y = m * min_x + b
            distance = distancia_euclidiana(min_x, min_y, xp, yp)

    except ZeroDivisionError:
        max_y = max(y1, y2)
        min_y = min(y1, y2)
        max_x = max(x1 , x2)
        min_x = min(x1, x2)
        if x1 == x2:
            if yp >= min_y and yp <= max_y:
                distance = abs(xp - x1)
            elif yp > max_y:
                distance = distancia_euclidiana(x1, max_y, xp, yp)
            else:
                distance = distancia_euclidiana(x1, min_y, xp, yp)
        elif y1 == y2:
            if xp >= min_x and xp <= max_x:
                distance = abs(yp - y1)
            elif xp > max_x:
                distance = distancia_euclidiana(max_x, y1, xp, yp)
            else:
                distance = distancia_euclidiana(min_x, y1, xp, yp)
    return distance

def calcular_angulo_entre_rectas(m1, m2):
    angulo = math.atan(abs((m2 - m1) / (1 + m1 * m2)))

    if m1 < 0 and m2 > 0:
        angulo = math.pi - angulo
    elif m1 > 0 and m2 < 0:
        angulo = math.pi - angulo
    elif m1 < 0 and m2 < 0:
        angulo = -angulo

    return angulo

def evaluacion(grafo, pares_de_puntos):
    sumatoria = 0
    leng = 0
    for inicio ,destino in pares_de_puntos:
        leng += 1
        sumatoria += busqueda_rapida(grafo, inicio, destino)
    sumatoria /= 5.5555 
    # Para tener el tiempo, ya que la distancia es irrelevante en nuestro problema.
    # En este caso transformamos la distancia al tiempo que toma recorrerla a 20km/h
    # ya que, la distancia es la misma para buenas o malas vias. La evaluacion se hace sobre distancia por que
    # con esta unidad es mas comodo trabajar por ejemplo en los algoritmos recursivos, con los metros restantes
    # seria raro tener el algoritmo en terminos de "segundos" restantes. Cuando "mejoramos" las vias, estamos
    # haciendo un truco de "reducir la distancia" y aunque eso no sea preciso, el resultado es el mismo, ya que
    # cuando aumentamos la velocidad * 3, el tiempo se reduce * 3, asi que no hay problema con esta sutileza. Y    
    # tener un grafo de tiempo y de distancia seria muy engorroso sabiendo que el factor de cambio es 
    # tiempo * vel(5.55555 m/s) = distancia, al reducir la distancia, el efecto en el tiempo es el mismo

    return sumatoria / leng


def evaluacion_n_grafo(grafo, vias_mejoradas, pares_de_puntos):
    n_grafo = copy.deepcopy(grafo)
    for via in vias_mejoradas:
        n_grafo[via] /= 3 # La distancia / tiempo, disminuye por 3

    return evaluacion(n_grafo, pares_de_puntos)
    

    #return promedio_viajes

def crear_cuadrantes(nodos):
    """
    Separar los nodos de un grafo en 9 cuadrantes:

        1 - NorOccidente
        2 - Norte
        3 - NorOriente
        4 - Occidente
        5 - Centro
        6 - Oriente
        7 - SurOccidente
        8 - Sur
        9 - SurOriente

    Para luego seleccionar un punto aleatorio del cuadrante
    """

    coordenadas_x = {e: d["x"] for e, d in nodos}
    coordenadas_y = {e: d["y"] for e, d in nodos}

    llaves_por_eje_x = sorted(coordenadas_x, key=lambda x: coordenadas_x[x])
    llaves_por_eje_y = sorted(coordenadas_y, key=lambda x: coordenadas_y[x])

    # Separar los nodos en tercios para cada eje
    longitud_x = len(llaves_por_eje_x)
    longitud_y = len(llaves_por_eje_y)

    separacion_1x = llaves_por_eje_x[:longitud_x // 3]
    separacion_2x = llaves_por_eje_x[longitud_x // 3:longitud_x * 2 // 3]
    separacion_3x = llaves_por_eje_x[longitud_x * 2 // 3:]
    separacion_x = [separacion_1x, separacion_2x, separacion_3x]

    separacion_1y = llaves_por_eje_y[:longitud_y // 3]
    separacion_2y = llaves_por_eje_y[longitud_y // 3:longitud_y * 2 // 3]
    separacion_3y = llaves_por_eje_y[longitud_y * 2 // 3:]
    separacion_y = [separacion_1y, separacion_2y, separacion_3y]

    cuadrantes = {}

    cuadrantes[1] = set(separacion_x[0]) & set(separacion_y[2])  # NorOccidente
    cuadrantes[2] = set(separacion_x[1]) & set(separacion_y[2])  # Norte
    cuadrantes[3] = set(separacion_x[2]) & set(separacion_y[2])  # NorOriente
    cuadrantes[4] = set(separacion_x[0]) & set(separacion_y[1])  # Occidente
    cuadrantes[5] = set(separacion_x[1]) & set(separacion_y[1])  # Centro
    cuadrantes[6] = set(separacion_x[2]) & set(separacion_y[1])  # Oriente
    cuadrantes[7] = set(separacion_x[0]) & set(separacion_y[0])  # SurOccidente
    cuadrantes[8] = set(separacion_x[1]) & set(separacion_y[0])  # Sur
    cuadrantes[9] = set(separacion_x[2]) & set(separacion_y[0])  # SurOriente

    return cuadrantes


def busqueda_rapida(grafo, start, goal):
    """
    Este algoritmo NO fue desarrollado ni implementado por nosotros, es un algoritmo basado en A*, y es por decirlo asi
    una buena aproximacion de Djastktra pero con un orden de complejidad menor, lo cual sera efectivo ya que
    nuestro programa necesita hacer muchas simulaciones, esta implementacion ayudara a reducir los tiempos para
    todos los algoritmos
    """
    open_set = [] 
    heapq.heappush(open_set, (0, start))
    
    came_from = {}  
    g_score = {start: 0}  
    
    while open_set:
        current_cost, current = heapq.heappop(open_set)
        
        if current == goal:
            return current_cost
        
        for (u, v), cost in grafo.items():
            if u == current:
                neighbor = v
                tentative_g_score = g_score[current] + cost
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    heapq.heappush(open_set, (tentative_g_score, neighbor))
    
    return float('inf')  # No se encontró un camino


def formatear_grafo_dijkstra(grafo_original):
    """
    Como cambiamos la busqueda_recursiva por un algoritmo basado en dijkstra, 
    el formato del grafo es distinto

    grafo_anterior_ejemplo = {
        ('A', 'B'): 1,
        ('A', 'C'): 4,
        ('B', 'C'): 2,
        ('B', 'D'): 5,
        ('C', 'D'): 1
    }

    grafo_formato_nuevo = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    """
    # Inicializar un nuevo grafo en el formato deseado
    grafo_nuevo = {}
    
    for (nodo1, nodo2), peso in grafo_original.items():
        if nodo1 not in grafo_nuevo:
            grafo_nuevo[nodo1] = {}
        if nodo2 not in grafo_nuevo:
            grafo_nuevo[nodo2] = {}
        
        # Añadir las conexiones bidireccionales
        grafo_nuevo[nodo1][nodo2] = peso
        grafo_nuevo[nodo2][nodo1] = peso
    
    return grafo_nuevo



def busqueda_intermedia(grafo_viejo, inicio, objetivo):
    """ALGORITMO BASADO EN DIJASKTRA, NOS TOCO USARLO SOBRE EL ALGORITMO ANTERIOR DE BUSQUEDA_RECURSIVA
    YA QUE EL ALGORITMO DE BUSQUEDA RECURSIVA ERA SIMPLEMENTE INVIABLE IMPLEMENTARLO CON GRAFOS GRANDES
    """
    grafo = formatear_grafo_dijkstra(grafo_viejo)
    
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    previos = {nodo: None for nodo in grafo}
    cola_prioridad = [(0, inicio)]  # (distancia, nodo)
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == objetivo:
            # Reconstruir el camino
            camino = []
            while previos[nodo_actual] is not None:
                camino.append((previos[nodo_actual], nodo_actual))
                nodo_actual = previos[nodo_actual]
            camino.reverse()
            return camino, distancias[objetivo]
        
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        for vecino, peso in grafo.get(nodo_actual, {}).items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                previos[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    return [], float('inf')  # No se encontró un camino


def busqueda_antigua_recursiva(nodo_actual, nodo_objetivo, grafo, visitados, camino, distancias, c = 0):
    """
    Inicialmente estaba contemplado utilizar este algoritmo para
    nuestro programa sin embargo para grafos grandes es simplemente
    demasiado ineficiente, dejamos el algoritmo ya que es muy simple 
    e incluso, sin embargo esta inutilizado y fue reemplazado por un 
    algoritmo usando djasktra y colas de prioridad.    
    """
    
    if nodo_actual == nodo_objetivo:
        return camino, sum(distancias)

    if nodo_actual in visitados:
        return [], float("inf")

    vecinos = {}
    for tupla, peso in grafo.items():
        if nodo_actual in tupla:
            vecino = tupla[0] if tupla[1] == nodo_actual else tupla[1]
            vecinos[vecino] = peso

    if not vecinos:
        return [], float("inf")

    camino_mas_corto = []
    distancia_optima = float("inf")

    for vecino, peso in vecinos.items():
        # Asegúrate de que `distancias` es una lista
        nuevo_camino, nueva_distancia = busqueda_recursiva(
            vecino, nodo_objetivo, grafo, 
            visitados + [nodo_actual], 
            camino + [(nodo_actual, vecino)], 
            distancias + [peso], 
            c = 1
        )
        
        # `nueva_distancia` debería ser un número, sumando las distancias en el camino
        if nueva_distancia < distancia_optima:
            distancia_optima = nueva_distancia
            camino_mas_corto = nuevo_camino

    print("Resultado busqueda recursiva: \n camino corto:", camino_mas_corto, "\n distancia_optima: ", distancia_optima)
    return camino_mas_corto, distancia_optima


def algoritmo_voraz(puntajes, G, presupuesto):
    # Obtener todas las aristas y distancias del grafo
    aristas = G.edges(data=True)
    distancias = { (inicio, fin): info["length"] for inicio, fin, info in aristas }
    
    aristas_ordenadas = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
    
    presupuesto_restante = presupuesto
    aristas_seleccionadas = []
    
    for arista, puntuacion in aristas_ordenadas:
        if arista in distancias:
            distancia = distancias[arista]
            if distancia <= presupuesto_restante:
                aristas_seleccionadas.append(arista)
                presupuesto_restante -= distancia
    
    return aristas_seleccionadas

def puntuacion(arista, concurrencia, caminos , presupuesto, k):
    # FUNCION PARA VER QUE ARISTAS SON MAS UTILES
    #puntuacion = a + b, a es la parte de la concurrencia y b la parte zonas
    # concurrencia == en cuantos caminos esta mi nodo
    if concurrencia == 0:
        a = 0
    else:
        a = 2 ** (concurrencia - 1)


    numero_de_caminos = 0
    for camino in caminos:
        algo = None# medir la distancia
        if algo:
            numero_de_caminos += 1

    coseno = abs()#usar numpy
    coseno += 1
    coseno /= 2 # el rango pasa a ser de 0.5 a 1

    b = numero_de_caminos * k * coseno

    return a + b