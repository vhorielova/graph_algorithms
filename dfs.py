# from graph import Graph


def dfs_alg(u, visited, graph):
    print(u)
    visited[u] = 1
    for v in graph.adjacencyList[u]:
        if visited[v] != 1:
            dfs_alg(v, visited, graph)


def dfs(graph, u = None):
    visited = [0 for i in range(graph.numberOfVertices)]
    if(u == None):
        for i in range(graph.numberOfVertices):
            if visited[i] == 0:
                dfs_alg(i, visited, graph)
    else:
        dfs_alg(u, visited, graph)

