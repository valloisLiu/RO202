import numpy as np
import graph
import sys

def main():

    # Le poids des arcs de ce graphe correspondent aux capacités
    g = example()

    # Le poids des arcs de ce graphe correspondent au flot
    flow = fordFulkerson(g, "s", "t")

    print(flow)
    
# Fonction créant un graphe sur lequel sera appliqué l'algorithme de Ford-Fulkerson
def example():
        
    g = graph.Graph(np.array(["s", "a", "b", "c", "d", "e", "t"]))

    g.addArc("s", "a", 8)
    g.addArc("s", "c", 4)
    g.addArc("s", "e", 6)
    g.addArc("a", "b", 10)
    g.addArc("a", "d", 4)
    g.addArc("b", "t", 8)
    g.addArc("c", "b", 2)
    g.addArc("c", "d", 1)
    g.addArc("d", "t", 6)
    g.addArc("e", "b", 4)
    g.addArc("e", "t", 2)
    
    return g

# Fonction appliquant l'algorithme de Ford-Fulkerson à un graphe
# Les noms des sommets sources est puits sont fournis en entrée
def fordFulkerson(g, sName, tName):

    """
    Marquage des sommets du graphe:
     - mark[i] est égal à +j si le sommet d'indice i peut être atteint en augmentant le flot sur l'arc ji
     - mark[i] est égal à  -j si le sommet d'indice i peut être atteint en diminuant le flot de l'arc ji
     - mark[i] est égal à sys.float_info.max si le sommet n'est pas marqué
    """
    mark = [0] * g.n
    
    # Récupérer l'indice de la source et du puits
    s = g.indexOf(sName)
    t = g.indexOf(tName)
    
    # Créer un nouveau graphe contenant les même sommets que g
    flow = graph.Graph(g.nodes)

    # Récupérer tous les arcs du graphe 
    arcs = g.getArcs()

    # Ajouter votre code ici
    # ... 
    for i in range(flow.n):
        for j in range(flow.n):
            flow.adjacency[i][j] = 0
    
    max_flow = 0  # initialize the max flow
    
    # Find all the way from s to t by using BFS algorithme
    # We cam also use DFS algorithme, but it isn't as efficient as BFS
    while True:
        queue = [s]
        visited = [-1] * g.n
        visited[s] = s
        path_flow = float('100000000')
        
        while queue:
            u = queue.pop(0)
            for v in range(g.n):
                if g.adjacency[u][v] - flow.adjacency[u][v] > 0 and visited[v] == -1:
                    queue.append(v)
                    visited[v] = u
                    path_flow = min(path_flow, g.adjacency[u][v] - flow.adjacency[u][v])
                    
        if visited[t] == -1: 
            break

        v = t
        while v != s:
            u = visited[v]
            flow.adjacency[u][v] += path_flow
            flow.adjacency[v][u] -= path_flow
            v = u
        
        max_flow += path_flow  # calcul the max flow
    
    # Set the weight of each arc as the final flow
    for i in range(flow.n):
        for j in range(flow.n):
            if flow.adjacency[i][j] < 0:
                flow.adjacency[i][j] = 0
    print("The max flow is :",max_flow)
    print("The flow that we obtain is:")
    return flow
   
if __name__ == '__main__':
    main()
