# BFS with selected and non-selected starting vertex
def bfs(graph, u=None):
    if u is None:
        u = 0

    visited = [0 for i in range(graph.numberOfVertices)]
    visited[u] = 1

    q = [u]

    while (q):
        u = q.pop(0)
        for v in graph.adjacencyList[u]:
            if visited[v] == 0:
                print(v)
                visited[v] = 1
                q.append(v)
