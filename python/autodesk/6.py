graph = {
    "A": ["B", "D"],
    "B": [],
    "C": [],
    "D": ["C"]
}

def bfs(start, graph, visited = set()):
    queue = [start]

    while len(queue) != 0:
        u = queue[0]

        if u in visited:
            continue
        
        visited.add(u)
        print(u)

        del queue[0]

        for c in graph[u]:
            queue.append(c)

print(bfs("A", graph))

def binary_search(nums, target):
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1