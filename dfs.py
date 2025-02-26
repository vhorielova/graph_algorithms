# from graph import Graph

# recursive DFS algorithm
def dfs_alg(u, visited, graph):
    print(u)
    visited[u] = 1
    for v in graph.adjacencyList[u]:
        if visited[v] != 1:
            dfs_alg(v, visited, graph)


# DFS with selected and non-selected starting vertex
def dfs(graph, u=None):
    visited = [0 for i in range(graph.numberOfVertices)]
    if u is None:
        for i in range(graph.numberOfVertices):
            if visited[i] == 0:
                dfs_alg(i, visited, graph)
    else:
        dfs_alg(u, visited, graph)
