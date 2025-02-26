from graph import Graph
from dfs import dfs
from bfs import bfs

numberOfVertices = 4
edges = [[1, 2], [2, 3], [1, 3], [3, 4]]
isOriented = False
graph = Graph(numberOfVertices, edges, isOriented)
print(graph.__str__())
#dfs(graph, 2)
bfs(graph, 2)
