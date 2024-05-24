import numpy as np
import graph
import sys

def main():
    # Créer un graphe contenant les sommets a, b, c, d, e, f, g 
    g = graph.Graph(np.array(["a", "b", "c", "d", "e", "f", "g"]))

    # Ajouter les arêtes
    g.addEdge("a", "b",  1.0)
    g.addEdge("a", "c",  3.0)
    g.addEdge("b", "c",  2.0)
    g.addEdge("b", "d",  5.0)
    g.addEdge("b", "e",  7.0)
    g.addEdge("b", "f",  9.0)
    g.addEdge("c", "d",  4.0)
    g.addEdge("d", "e",  6.0)
    g.addEdge("d", "g", 12.0)
    g.addEdge("e", "f",  8.0)
    g.addEdge("e", "g", 11.0)
    g.addEdge("f", "g", 10.0)
    
    # Obtenir un arbre couvrant de poids minimal du graphe
    tree = kruskal(g)
    print("The tree after Kruskal function is:")
    # S'il existe un tel arbre (i.e., si le graphe est connexe)
    if tree != None:
        
        # L'afficher
        print(tree)
    
    else:
        print("Pas d'arbre couvrant")

# Applique l'algorithme de Kruskal pour trouver un arbre couvrant de poids minimal d'un graphe
# Retourne: Un arbre couvrant de poids minimal du graphe ou None s'il n'en existe pas
def kruskal(g):
    
    # Créer un nouveau graphe contenant les mêmes sommets que g
    tree = graph.Graph(g.nodes)
    
    # Nombre d'arêtes dans l'arbre
    addedEdges = 0
    
    # Récupérer toutes les arêtes de g
    edges = g.getEdges()
    
    # Trier les arêtes par poids croissant
    edges.sort()
    parents = {i: i for i in range(g.n)}
    new_list = {i: 0 for i in range(g.n)}

    def cherche(i):
        if parents[i] != i:
            parents[i] = cherche(parents[i])
        return parents[i]

    def union(i, j):
        begin = cherche(i)
        end = cherche(j)
        if begin != end:
            if new_list[begin] > new_list[end]:
                parents[end] = begin
            elif new_list[begin] < new_list[end]:
                parents[begin] = end
            else:
                parents[end] = begin
                new_list[begin] += 1

    # Récupérer toutes les arêtes de g et les trier par poids croissant
    edges = sorted(edges, key=lambda edge: edge.weight)

    for edge in edges:
        root_id1 = cherche(edge.id1)
        root_id2 = cherche(edge.id2)
        if root_id1 != root_id2:
            tree.addCopyOfEdge(edge)
            union(root_id1, root_id2)
            addedEdges += 1
            if addedEdges == g.n - 1:
                break
    
    if addedEdges == g.n - 1:
        return tree
    else:
        return None

if __name__ == '__main__':
    main()
