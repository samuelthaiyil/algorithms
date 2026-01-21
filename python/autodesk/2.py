def comb_sum(candidates, target):
    res = []
    n = len(candidates)

    def dfs(start, path, total):
        if total == target:
            res.append(path.copy())
            print(f"good path {path}")
            return
        
        if total > target:
            print(f"bad path {path}")
            return
        
        for i in range(start, n):
            dfs(i, path + [candidates[i]], total + candidates[i])
        
    dfs(0, [], 0)
    return res

print(comb_sum([2,3,6,7], 7))