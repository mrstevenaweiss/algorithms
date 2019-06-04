
#inputs : a graph 
#output : an ordered list where u goes before v given an edge (u, v)
#test : 1, 3, 2, 4, 5, 6, 11 
def topological_sort(G):
    sorted_graph = [0] * 12
    
    for vertex, adjacent in G.items():
        for number in adjacent:
            # print(sorted_graph[number])
            sorted_graph[number] += 1
    return sorted_graph
incomplete...
# 4. Make a list next consisting of all vertices u such that
# in-degreeŒu D 0.
# 5. While next is not empty, do the following:
# A. Delete a vertex from next, and call it vertex u.
# B. Add u to the end of the linear order.
# C. For each vertex v adjacent to u:
# i. Decrement in-degreeŒv.
# ii. If in-degreeŒv D 0, then insert v into the next list.
# 6. Return the linear order.
graph = {
    1: [3],
    2: [4],
    3: [4, 5],
    4: [6],
    5: [6],
    6: [7, 11]
}
topological_sort(graph)
