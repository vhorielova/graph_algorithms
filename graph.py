class Graph:
    def __init__(self, numberOfVertices, edges, isOriented):
        self.numberOfVertices = numberOfVertices
        self.edges = edges
        self.isOriented = isOriented
        self.adjacencyList = self.toAdjacencyList(edges, isOriented)
        self.adjacencyMatrix = self.toAdjacencyMatrix(numberOfVertices, edges, isOriented)

    def toAdjacencyList(self, edges, isOriented):
        adjacencyList = {}
        for u, v in edges:
            if u in adjacencyList:
                adjacencyList[u].append(v)
            else:
                adjacencyList[u] = [v]
            if not isOriented:
                if v in adjacencyList:
                    adjacencyList[v].append(u)
                else:
                    adjacencyList[v] = [u]
        return adjacencyList

    def toAdjacencyMatrix(self, numberOfVertices, edges, isOriented):
        adjacencyMatrix = [[0 for _ in range(numberOfVertices)] for _ in range(numberOfVertices)]
        for u, v in edges:
            adjacencyMatrix[u - 1][v - 1] = 1
            if not isOriented:
                adjacencyMatrix[v - 1][u - 1] = 1
        return adjacencyMatrix
    def __str__(self):
        return (f"Number of vertices: {self.numberOfVertices}\n"
                f"Edges: {self.edges}\n"
                f"Adjacency matrix{self.adjacencyMatrix}\n"
                f"Adjacency list: {self.adjacencyList}\n")