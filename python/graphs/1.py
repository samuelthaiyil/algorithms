def traverseGraph(start, graph):
    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)
    dfs(start)

