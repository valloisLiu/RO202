import graph
import sys

def main():
    cities = []
    cities.append("Paris")
    cities.append("Hambourg")
    cities.append("Londres")
    cities.append("Amsterdam")
    cities.append("Edimbourg")
    cities.append("Berlin")
    cities.append("Stockholm")
    cities.append("Rana")
    cities.append("Oslo")

    g = graph.Graph(cities)
    
    g.addArc("Paris", "Hambourg", 7)
    g.addArc("Paris",  "Londres", 4)
    g.addArc("Paris",  "Amsterdam", 3)
    g.addArc("Hambourg",  "Stockholm", 1)
    g.addArc("Hambourg",  "Berlin", 1)
    g.addArc("Londres",  "Edimbourg", 2)
    g.addArc("Amsterdam",  "Hambourg", 2)
    g.addArc("Amsterdam",  "Oslo", 8)
    g.addArc("Stockholm",  "Oslo", 2)
    g.addArc("Stockholm",  "Rana", 5)
    g.addArc("Berlin",  "Amsterdam", 2)
    g.addArc("Berlin",  "Stockholm", 1)
    g.addArc("Berlin",  "Oslo", 3)
    g.addArc("Edimbourg",  "Oslo", 7)
    g.addArc("Edimbourg",  "Amsterdam", 3)
    g.addArc("Edimbourg",  "Rana", 6)
    g.addArc("Oslo",  "Rana", 2)
    
    # Applique l'algorithme de Dijkstra pour obtenir une arborescence
    tree = dijkstra(g, "Paris")
    print(tree)
    # print("The total cost is:")
    # sum = 0
    # for i in pi:
    #     sum += i
    # print (sum)

def dijkstra(g, origin):

   r = g.indexOf(origin)

   # Next node considered 
   pivot = r

   v2 = []
   v2.append(r)
   v2 = [False] * g.n  
   pred = [-1] * g.n   
   pi = [sys.float_info.max] * g.n  
   pi[r] = 0

   for _ in range(g.n):
        petit = sys.float_info.max
        u = -1
        for i in range(g.n):
            if not v2[i] and pi[i] < petit:
                petit = pi[i]
                u = i
        v2[u] = True
        for v in range(g.n):
            if g.adjacency[u][v] != 0 and not v2[v]:
                alt = pi[u] + g.adjacency[u][v]
                if alt < pi[v]:
                    pi[v] = alt
                    pred[v] = u

   for i in range(g.n):
        path = []
        node = i
        while node != -1:
            path.append(g.nodes[node])
            node = pred[node]
        path.reverse()
#    path_fin = list(len(path))
#    for i in len(path):
#        path_fin[i] = path[i]
#    path_fin[-1] = "Rana"
   path.append('Rana')
   return pi, path

   
if __name__ == '__main__':
    main()
