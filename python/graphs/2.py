from math import sqrt

def maximumDetonation(bombs):
    n = len(bombs)
    graph = {i: list() for i in range(n)}

    # build graph for add bomb j that is within blast radius of bomb i
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            x1, y1, r = bombs[i]
            x2, y2, _ = bombs[j]

            d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

            if r >= d:
                graph[i].append(j)
    
    answer = 0

    def dfs(node, visited):
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour, visited)
        
        return len(visited)
    
    for i in range(n):
        visited = set()
        answer = max(answer, dfs(i, visited))
    
    return answer

print(maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))
